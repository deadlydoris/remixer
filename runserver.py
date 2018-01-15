#!/usr/bin/env python3
from flask import Flask, render_template, request
from pprint import pprint
import random 

app = Flask("__name__")

def mash(music_file1, music_file2, splice_length_1, splice_length_2):
    print(music_file1)
    print(splice_length_2)
    return ""

@app.route('/ufos')
def talk_about_ufos():
    return "My crazy theory about UFOS is that there are " + str(random.randint(100, 10000)) + " of them"

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/getmashed', methods=['POST'])
def prepare_to_mash():
    formdata = request.form.to_dict
    splice_length_1 = int(request.form['splice_length_1'])
    splice_length_2 = int(request.form['splice_length_2'])
    music_file_1 = request.files["music_file_1"]
    music_file_2 = request.files["music_file_2"]
    mash(music_file_1, music_file_2, splice_length_1, splice_length_2)
    return ""




app.run(
       host="0.0.0.0",
       port=8080,
       debug=True
)



