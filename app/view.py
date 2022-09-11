from flask import render_template

from app import app


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/<string:path_var>')
def name(path_var):
    print(path_var)
    return render_template('home.html', name=path_var)
