from flask import redirect, url_for
from flask_admin import Admin, AdminIndexView
from flask_admin.contrib.sqla import ModelView
from flask_admin.menu import MenuLink
from flask_login import LoginManager, current_user

from app import app, db
from app.models import UserModel, OwnerModel, PetModel


class OwnerModelView(ModelView):
    form_excluded_columns = 'pets'


class UserModelView(ModelView):

    def is_accessible(self):
        if current_user and current_user.is_authenticated:
            return current_user.admin
        else:
            return True

    def inaccessible_callback(self, name, **kwargs):
        redirect(url_for('home'))


class MyAdminIndexView(AdminIndexView):

    def is_accessible(self):
        return current_user.is_authenticated

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('home'))


admin = Admin(app, index_view=MyAdminIndexView)
login = LoginManager(app)


@login.user_loader
def load_user(user_id):
    return UserModel.query.get(user_id)


admin.add_view(UserModelView(UserModel, db.session, 'User'))
admin.add_view(OwnerModelView(OwnerModel, db.session, "Owner"))
admin.add_view(ModelView(PetModel, db.session, 'Pet'))

admin.add_link(MenuLink('Logout', '/logout'))
