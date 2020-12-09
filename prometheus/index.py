"""Main module for """
from flask import render_template, request

from prometheus import app

from .constant import SECRET_KEY
from .forms import MyForm

app.secret_key = SECRET_KEY


@app.route("/", methods=["GET", "POST"])
def index():
    form = MyForm(request.form)
    return render_template("index.html", form=form)
