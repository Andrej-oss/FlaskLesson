from flask import render_template, redirect, url_for
from flask_login import login_user, logout_user

from app import app
from app.models import UserModel


@app.route('/')
def home():
    return redirect(url_for('admin.index'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')


@app.route('/login/user')
def login_user_in():
    user = UserModel.query.get(2)
    login_user(user)
    return redirect('/admin')


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))
