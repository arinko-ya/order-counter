from datetime import datetime

from flask_wtf import FlaskForm
from wtforms import SubmitField, DateField
from wtforms.validators import DataRequired


class InputDateForm(FlaskForm):
    input_date = DateField('Input Date', validators=[DataRequired()],
                           default=datetime.today())
    submit = SubmitField('Start')
