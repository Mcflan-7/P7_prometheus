from flask_wtf import FlaskForm
from wtforms import SubmitField, TextAreaField


class MyForm(FlaskForm):
    message = TextAreaField("Votre message")
    submit = SubmitField("Envoyer")
