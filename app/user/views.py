from flask import Blueprint, render_template, request, redirect, url_for

from app import app, db
from app.user.forms import UserForm
from app.user.models import User

# user = Blueprint('users', __name__, static_folder='static', template_folder='templates', url_prefix='/user')


@app.route('/', methods=['GET', 'POST'])
def get_users():
    users = User.query.all()
    if request.method == 'POST':
        data = dict(request.form)
        data.pop('save')
        print(data)
        user = User(**data)
        db.session.add(user)
        db.session.commit()
        users = User.query.all()
    return render_template('index.html', form=UserForm(request.form), users=users)


@app.route('/<int:index>')
def delete(index):
    User.query.filter_by(id=index).delete()
    db.session.commit()
    return redirect(url_for('get_users'))


@app.route('/<string:name>')
def get_user_by_name(name):
    return str(User.query.filter_by(name=name).first())
