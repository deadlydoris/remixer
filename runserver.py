#!/usr/bin/env python3
from flask import Flask, render_template
import random 

app = Flask("__name__")

@app.route('/ufos')
def talk_about_ufos():
    return "My crazy theory about UFOS is that there are " + str(random.randint(100, 10000)) + " of them"
@app.route('/')
def index():
    return render_template("index.html")

app.run(
       host="0.0.0.0",
       port=8080,
       debug=True
)



