from flask import render_template, flash, redirect, url_for, request
from flask_login import login_required

from app import db
from app.models import Item, Genre
from app.order_counter import bp
from app.order_counter.forms import EditItemForm, InputDateForm


@bp.route('/', methods=['GET', 'POST'])
@bp.route('/index', methods=['GET', 'POST'])
def input_date():
    form = InputDateForm()
    if form.validate_on_submit():

    return render_template('order_counter/input_date.html', form=form)


@bp.route('/order_counter', methods=['GET', 'POST'])
def order_counter():
    item_list = Item.get_sale_list()
    return render_template('order_counter/order_counter.html',
                           title='order_counter',
                           item_list=item_list)


@bp.route('/edit_item', methods=['GET', 'POST'])
@login_required
def edit_item():
    genre_list = Genre.query.all()
    item_list = Item.query.all()
    form = EditItemForm()
    if form.validate_on_submit():
        item = Item(name=form.item_name.data,
                    genre_id=form.genre.data,
                    price=form.price.data,
                    is_sale=form.is_sale.data)
        db.session.add(item)
        db.session.commit()
        flash('Menu addition completed')
        return redirect(url_for('order_counter.edit_item'))
    return render_template('order_counter/edit_menu.html',
                           title='Add Menu',
                           form=form,
                           item_list=item_list,
                           genre_list=genre_list)


@bp.route('update_item/<item_id>', methods=['GET', 'POST'])
@login_required
def update_item(item_id):

    item = {'id': item_id,
            'name': request.form.get(f'name_{item_id}'),
            'genre_id': request.form.get(f'genre_id_{item_id}'),
            'price': request.form.get(f'price_{item_id}'),
            'is_sale': request.form.get(f'is_sale_{item_id}') == 'True'}

    Item.update_item(**item)
    flash('Item update is complete!')
    return redirect(url_for('order_counter.edit_item'))
