from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import os, sys


app = Flask(__name__, template_folder="../data/template", static_folder="../data/static")

@app.route('/', methods=["POST", "GET"])
def Texter():
    return render_template('page_1.html')


@app.route('/upload')
def upload_file():
    return render_template('Uploader.html')




app.run(host='0.0.0.0', port=8093)