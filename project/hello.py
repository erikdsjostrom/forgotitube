import os
from flask import Flask
from flask import url_for
from flask import render_template
from flask import request
#from get_new_video import get_new_video
from rotate_background import rotate_background

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello World!'
