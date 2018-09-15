from flask_wtf import FlaskForm
from wtforms import SubmitField, DateField
from wtforms.validators import DataRequired


class InputDateForm(FlaskForm):
    sold_at = DateField('Input Date', validators=[DataRequired()])
    submit = SubmitField('Submit')
