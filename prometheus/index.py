"""Main module for """
from flask import Flask, render_template, request

from .constant import SECRET_KEY
from .forms import MyForm

app = Flask(__name__)
app.secret_key = SECRET_KEY


@app.route("/")
def index():
    form = MyForm(request.form)
    return render_template("index.html", form=form)

if __name__ == "__main__":
    app.run()