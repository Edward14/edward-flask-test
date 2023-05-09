from flask import render_template

def hello_world():
    return "Hello, I'm trying"

def index():
    return render_template('index.html') 