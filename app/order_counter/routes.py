from flask import render_template, flash, redirect, url_for, session
from flask_login import login_required

from app.order.models import Order
from app.item.models import Item
from app.order_counter import bp
from app.order_counter.forms import InputDateForm


@bp.route('/index', methods=['GET', 'POST'])
@bp.route('/', methods=['GET', 'POST'])
@login_required
def order_counter():
    if not session.get('input_date'):
        return redirect(url_for('order_counter.order_counter_setting'))

    input_date = session['input_date']
    item_list = Item.get_sale_list()
    return render_template('order_counter/order_counter.html',
                           title='order_counter',
                           item_list=item_list,
                           input_date=input_date)


@bp.route('/setting', methods=['GET', 'POST'])
@login_required
def order_counter_setting():
    form = InputDateForm()
    if form.validate_on_submit():
        input_date = form.input_date.data
        order = Order.query.filter_by(date_sold=input_date).all()
        if order:
            flash('Already exists.', category='danger')
            return redirect(url_for('order_counter.order_counter_setting'))
        session['input_date'] = input_date
        return redirect(url_for('order_counter.order_counter'))
    return render_template('order_counter/input_date.html', form=form)
