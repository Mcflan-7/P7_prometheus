"""Main module to render form and data to the flask app """
from flask import render_template, request

from prometheus import app

from .constant import SECRET_KEY
from .forms import MyForm

app.secret_key = SECRET_KEY


@app.route("/", methods=["GET", "POST"])
def index():
    """display the form and information for the client to the main
    index page.

    **Templates**

    :template:`prometheus/index.html`
    """
    form = MyForm(request.form)
    return render_template("index.html", form=form)
