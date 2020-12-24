"""Main module to render form and data to the flask app """
from flask import render_template, request, jsonify

from prometheus import app

from .bot import BotPy
from .constant import SECRET_KEY
from .forms import FormBot

app.secret_key = SECRET_KEY


@app.route("/")
def index():
    """display the form and information for the client to the main
    index page.

    **Templates**

    :template:`prometheus/index.html`
    """

    return render_template(
        "index.html")

@app.route("/ajax", methods=["POST"])
def ajax():
    """Received data from a python module and
    return a jsonify content to the client
    """
    question = request.form["question"]
    bot = BotPy(question)
    response = bot.give_answer_for_client()
    return jsonify(response)