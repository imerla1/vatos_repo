from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from wtforms import StringField, SubmitField

class InputField(FlaskForm):
    num_input = StringField("Enter Number", validators=[DataRequired(message="Please Enter value for input")])
    submit = SubmitField("Submit")