from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class GenreAdditionalForm(FlaskForm):
    genre = StringField('Genre', validators=[DataRequired()])
    submit = SubmitField('Add')

