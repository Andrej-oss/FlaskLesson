from flask import render_template

from app import app

isTrue = True

users = ['joe', 'poo', 'foo', 'jack']


@app.route('/')
def home():
    return render_template('index.html')

