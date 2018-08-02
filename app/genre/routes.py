from flask import render_template, redirect, url_for, flash, request
from flask_login import login_required

from app.genre.models import Genre
from app.genre import bp
from app.genre.forms import GenreAdditionalForm


@bp.route('/index', methods=['GET', 'POST'])
@bp.route('/', methods=['GET', 'POST'])
@login_required
def genre_edit():
    genre_list = Genre.query.all()
    form = GenreAdditionalForm()
    if form.validate_on_submit():
        status, message = Genre.add_genre(form.genre.data)
        category = 'info' if status == 'OK' else 'danger'

        flash(message, category=category)

        return redirect(url_for('genre.genre_edit'))
    return render_template('genre/genre_edit.html',
                           title='Genre Edit',
                           form=form,
                           genre_list=genre_list)


@bp.route('/update/<genre_id>', methods=['GET', 'POST'])
@login_required
def genre_update(genre_id: str):
    Genre.update(genre_id, request.form.get(f'genre_{genre_id}'))

    return redirect(url_for('genre.genre_edit'))
