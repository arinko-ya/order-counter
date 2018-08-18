from flask import render_template, redirect, url_for, flash, request
from flask_login import login_required

from app.genre.models import Genre
from app.genre import bp
from app.genre.forms import GenreAdditionalForm


@bp.route('/index', methods=['GET', 'POST'])
@bp.route('/', methods=['GET', 'POST'])
@login_required
def edit_genre():
    genre_list = Genre.query.all()
    form = GenreAdditionalForm()
    if form.validate_on_submit():
        result = Genre.add_genre(form.genre.data)
        flash(result.message, category=result.category)

        return redirect(url_for('genre.edit_genre'))
    return render_template('genre/edit_genre.html',
                           title='Genre Edit',
                           form=form,
                           genre_list=genre_list)


@bp.route('/update/<genre_id>', methods=['GET', 'POST'])
@login_required
def genre_update(genre_id: str):
    result = Genre.update(genre_id, request.form.get(f'genre_{genre_id}'))
    flash(result.message, category=result.category)

    return redirect(url_for('genre.edit_genre'))
