from collections import OrderedDict
from itertools import groupby

from flask import render_template, flash, redirect, url_for, session, request
from datetime import datetime

from flask_login import login_required

from app.item.models import Item
from app.order import bp
from app.order import registration
from app.order.forms import InputDateForm
from app.order.models import OrderHistory


@bp.route('/index', methods=['GET', 'POST'])
@bp.route('/', methods=['GET', 'POST'])
@login_required
def order_counter():
    item_list = Item.query.filter_by(
        is_active=True
    ).order_by(
        Item.genre_id,
        Item.is_high_priority.desc()
    )

    item_dict = OrderedDict()
    for key, group in groupby(item_list, key=lambda x: x.genre.name):
        item_dict[key] = list(group)

    form = InputDateForm()
    if form.validate_on_submit():
        sold_at = form.data.get('sold_at')
        add_list = []
        for item in Item.get_sale_list():
            add_list.append({
                'item': Item.query.get(item.id),
                'quantity': request.form.get(f'val{item.id}'),
                'sold_at': sold_at
            })
        result = registration.save_order(add_list)
        flash(result.message, category=result.category)

        return redirect(url_for('order.order_counter', sold_at=sold_at))

    return render_template('order/order_counter.html',
                           title='order',
                           item_dict=item_dict,
                           form=form,
                           sold_at=datetime.today().date())


@bp.route('/history')
@login_required
def history():
    order_summary_list = OrderHistory.calc()

    return render_template(
        'order/order_history.html',
        title='Order History',
        order_summary_list=order_summary_list
    )
