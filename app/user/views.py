from flask import Blueprint, render_template, request, redirect, url_for

from app.user.models import User

user = Blueprint('users', __name__, static_folder='static', template_folder='templates', url_prefix='/user')

users = []


@user.route('/', methods=['GET', 'POST'])
def get_users():
    print(request.args)
    if request.method == 'POST':
        name = request.form['name']
        surname = request.form['surname']
        users.append(User(**request.form))
        return render_template('user/index.html', name=name, surname=surname, users=users)
    return render_template('user/index.html')


@user.route('/<int:index>')
def delete(index):
    del users[index]
    return redirect(url_for('users.get_users'))
