from flask_wtf import FlaskForm
from wtforms import FloatField,SubmitField,TextField
from wtforms.validators import DataRequired

class Input_Form(FlaskForm):
	text = TextField('Enter Review below',validators=[DataRequired()])
	submit = SubmitField('Check****')

