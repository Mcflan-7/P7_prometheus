"""Prometheus app initialisation"""

from flask import Flask


from .constant import SECRET_KEY

app = Flask(__name__)
app.secret_key = SECRET_KEY
