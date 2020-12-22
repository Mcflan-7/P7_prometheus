from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired


class MyForm(FlaskForm):
    message = TextAreaField("Votre message")
    submit = SubmitField("Envoyer")
