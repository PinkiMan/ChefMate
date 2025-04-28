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

from utils.database import CookBook


app = Flask(__name__, template_folder="../data/template", static_folder="../data/static")


@app.route('/', methods=["POST", "GET"])
def homepage():
    cook_book = CookBook()

    # TODO: recommender get receipts

    best_trio = [cook_book.recipe_book.recipe_list[0], cook_book.recipe_book.recipe_list[0], cook_book.recipe_book.recipe_list[0]]

    return render_template('lobby_flask.html', recipe_list=cook_book.recipe_book.recipe_list)

@app.route('/recipe_adder.html',methods=["POST", "GET"])
def recipe_adder():
    return render_template('recipe_adder.html')


@app.route('/upload')
def upload_file():
    return render_template('Uploader.html')




app.run(host='0.0.0.0', port=8093)