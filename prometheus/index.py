"""Main module for """
from flask import Flask, render_template, request

from .constant import SECRET_KEY
from .forms import MyForm
from prometheus import app

app.secret_key = SECRET_KEY

@app.route("/", methods=["GET", "POST"])
def index():
    form = MyForm(request.form)
    return render_template("index.html", form=form)
