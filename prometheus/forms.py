from flask_wtf import FlaskForm
from wtforms import SubmitField, TextAreaField


class FormBot(FlaskForm):
    message = TextAreaField("Votre message")
    submit = SubmitField("Envoyer")
