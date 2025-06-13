from flask_wtf import FlaskForm  #base class which makes any class we write this into forms
from wtforms import StringField, SubmitField #stringfield creates a textinputbox whereas
#submit field adds a button to submit the form
from wtforms.validators import DataRequired

class ContactForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    message = StringField('Message', validators=[DataRequired()])
    submit = SubmitField('Submit')
