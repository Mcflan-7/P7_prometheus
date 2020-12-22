"""Main module to render form and data to the flask app """
from flask import render_template, request

from prometheus import app
from .bot import BotPy

from .constant import SECRET_KEY
from .forms import FormBot

app.secret_key = SECRET_KEY


@app.route("/", methods=["GET", "POST"])
def index():
    """display the form and information for the client to the main
    index page.

    **Templates**

    :template:`prometheus/index.html`
    """
    
    form = FormBot(request.form)
    bot = BotPy("paris")
    data = bot.get_question_from_client()
    story_title, story_extract, story_url = bot.give_answer_for_client(data)
    return render_template("index.html", form=form, title=story_title, extract=story_extract, url=story_url)
