__author__ = "Pinkas Matěj - Pinki"
__maintainer__ = "Pinkas Matěj - Pinki"
__email__ = "pinkas.matej@gmail.com"
__credits__ = []
__created__ = "24/04/2025"
__date__ = "24/04/2025"
__status__ = "Prototype"
__version__ = "0.1.0"
__copyright__ = ""
__license__ = ""

"""
Project: ChefMate
Filename: webserver.py
Directory: utils/
"""

from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import os, sys


app = Flask(__name__, template_folder="../data/template", static_folder="../data/static")


@app.route('/', methods=["POST", "GET"])
def homepage():
    return render_template('test_page_1.html')


@app.route('/upload')
def upload_file():
    return render_template('Uploader.html')




app.run(host='0.0.0.0', port=8093)