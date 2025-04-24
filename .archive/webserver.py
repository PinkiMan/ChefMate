from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import os, sys

Directory = "home/pi/Desktop/Raspberry-main"

app = Flask(__name__, template_folder="template", static_folder="static")


@app.route('/', methods=["POST", "GET"])
def Texter():
    Result = None
    if request.method == "POST":
        Input = request.form["nm"]
        print(Input)
        Result, Restart = Main(Input)
        if Restart:
            func = request.environ.get('werkzeug.server.shutdown')
            func()
            print("Restarting")
            print("Stopping webserver")
        elif "Vid" in Input:
            Command = Input.split("Vid")[1]
            Command = Command.replace(" ", "")
            return render_template('Video.html', file=Command)

    return render_template('Texter.html', Result=Result)


@app.route('/upload')
def upload_file():
    return render_template('Uploader.html')


@app.route('/uploader', methods=['GET', 'POST'])
def upload_file2():
    if request.method == 'POST':
        print("post")
        Input = request.form["nm"]
        print("input")
        f = request.files['file']
        print("f")
        """if not os.path.exists(Directory+Input):
            os.mkdir(Directory+Input)
        print(os.path.join(Directory+Input+"/",secure_filename(f.filename)))
        f.save(os.path.join(Directory+Input+"/",secure_filename(f.filename)))"""
        # f.save(f.filename)
        print("save")

        return 'file uploaded successfully'


@app.route('/Video')
def Video():
    return render_template('Video1.html')


app.run(host='0.0.0.0', port=8093)