from flask_wtf import FlaskForm
from wtforms import (StringField, BooleanField, SelectField,
                     IntegerField, SubmitField)
from wtforms.validators import DataRequired

from app.models import Genre


class EditItemForm(FlaskForm):
    item_name = StringField('Item name', validators=[DataRequired()])
    genre = SelectField('Genre', choices=Genre.get_genre_list(), validators=[DataRequired()])
    price = IntegerField('Price', validators=[DataRequired()])
    is_sale = BooleanField('Is sale')
    submit = SubmitField('Register')
    update = SubmitField('Update')
