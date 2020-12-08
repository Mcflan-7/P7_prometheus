"""Main module for """
from flask import Flask, render_template, request

from .forms import MyForm

from prometheus import app


@app.route("/")
def index():
    form = MyForm(request.form)
    return render_template("index.html", form=form)
