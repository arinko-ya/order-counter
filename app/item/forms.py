from flask_wtf import FlaskForm
from wtforms import (StringField, BooleanField, SelectField,
                     IntegerField, SubmitField)
from wtforms.validators import DataRequired

from app.genre.models import Genre


class EditItemForm(FlaskForm):
    item_name = StringField('Item name', validators=[DataRequired()])
    genre = SelectField('Genre', validators=[DataRequired()])
    price = IntegerField('Price', validators=[DataRequired()])
    is_sale = BooleanField('Is sale')
    submit = SubmitField('Register')
