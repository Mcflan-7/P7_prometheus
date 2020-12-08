from flask import Flask

app = Flask(__name__)


from prometheus import index  # noqa: E402 F401