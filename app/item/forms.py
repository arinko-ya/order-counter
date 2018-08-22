from flask_wtf import FlaskForm
from wtforms import (StringField, BooleanField, SelectField,
                     IntegerField, SubmitField)
from wtforms.validators import DataRequired


class EditItemForm(FlaskForm):
    item_name = StringField('Item Name', validators=[DataRequired()])
    genre = SelectField('Genre', validators=[DataRequired()])
    price = IntegerField('Price', validators=[DataRequired()])
    is_high_priority = BooleanField('Is high priority')
    submit = SubmitField('Register')
