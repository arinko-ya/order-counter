from flask import render_template, flash, redirect, url_for, session, request
from flask_login import login_required

from app.order.models import Order
from app.item.models import Item
from app.order import bp
from app.order.forms import InputDateForm


@bp.route('/index', methods=['GET', 'POST'])
@bp.route('/', methods=['GET', 'POST'])
@login_required
def order_counter():
    if not session.get('input_date'):
        return redirect(url_for('order.setting'))

    input_date = session['input_date']
    item_list = Item.get_sale_list()
    return render_template('order/order_counter.html',
                           title='order',
                           item_list=item_list,
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
