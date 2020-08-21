from flask import Flask

app = Flask(__name__)

import flaskr.dictionary.routes  # noqa: E402 F401
