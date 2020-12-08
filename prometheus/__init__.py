"""Prometheus app initialisation"""

from flask import Flask


from .constant import SECRET_KEY


app = Flask(__name__)
app.secret_key = SECRET_KEY

from app import errors  # pylint: disable=wrong-import-position
from app import routes