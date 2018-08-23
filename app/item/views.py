from flask import render_template, flash, redirect, url_for, request
from flask_login import login_required

from app import db
from app.genre.models import Genre
from app.item import bp
from app.item.forms import EditItemForm
from app.item.models import Item


@bp.route('/edit_item', methods=['GET', 'POST'])
@login_required
def edit_item():
    genre_list = Genre.get_genre_list()
    item_list = Item.query.all()
    form = EditItemForm()
    form.genre.choices = genre_list
    if form.validate_on_submit():
        item = Item(name=form.item_name.data,
                    genre_id=form.genre.data,
                    price=form.price.data,
                    is_high_priority=form.is_high_priority.data)
        db.session.add(item)
        db.session.commit()
        flash('Menu addition completed')
        return redirect(url_for('item.edit_item'))
    return render_template('item/edit_item.html',
                           title='Edit item',
                           form=form,
                           item_list=item_list,
                           genre_list=genre_list)


@bp.route('/update_item/<item_id>', methods=['GET', 'POST'])
@login_required
def update_item(item_id):
    item = {'id': item_id,
            'name': request.form.get(f'name_{item_id}'),
            'genre': Genre.query.get(request.form.get(f'genre_id_{item_id}')),
            'price': request.form.get(f'price_{item_id}'),
            'is_high_priority': request.form.get(f'is_high_priority_{item_id}') == 'True'}

    Item.update(**item)
    return redirect(url_for('item.edit_item'))


@bp.route('/update_active/<item_id>', methods=['POST'])
@login_required
def update_active(item_id):
    Item.update_active(item_id)
    return redirect(url_for('item.edit_item'))
