from collections import OrderedDict
from itertools import groupby

from flask import render_template, flash, redirect, url_for, session, request
from flask_login import login_required

from app.item.models import Item
from app.order import bp
from app.order.forms import InputDateForm
from app.order.models import Order, OrderHistory


@bp.route('/index', methods=['GET', 'POST'])
@bp.route('/', methods=['GET', 'POST'])
@login_required
def order_counter():
    if not session.get('input_date'):
        return redirect(url_for('order.setting'))

    input_date = session['input_date']

    item_list = Item.query.filter_by(
        is_active=True
    ).order_by(
        Item.genre_id,
        Item.is_high_priority.desc()
    )

    item_dict = OrderedDict()
    for key, group in groupby(item_list, key=lambda x: x.genre.name):
        item_dict[key] = list(group)

    return render_template('order/order_counter.html',
                           title='order',
                           item_dict=item_dict,
                           input_date=input_date)


@bp.route('/setting', methods=['GET', 'POST'])
@login_required
def setting():
    form = InputDateForm()
    if form.validate_on_submit():
        input_date = form.input_date.data
        order = Order.query.filter_by(sold_at=input_date).all()
        if order:
            flash('Already exists.', category='danger')
            return redirect(url_for('order.setting'))
        session['input_date'] = input_date
        return redirect(url_for('order.order_counter'))
    return render_template('order/input_date.html', form=form)


@bp.route('/register', methods=['POST'])
@login_required
def register_order():
    for item in Item.get_sale_list():
        Order.add_order(request.form.get(f'val_{item.id}'))


@bp.route('/history')
@login_required
def history():
    order_summary_list = OrderHistory.calc()

    return render_template(
        'order/order_history.html',
        title='Order History',
        order_summary_list=order_summary_list
    )
