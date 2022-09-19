from flask import redirect, url_for

from app import app
from app.owner.models import OwnerModel


@app.route('/')
def home():
    if OwnerModel.query.count():
        return redirect(url_for('owner.show_all'))
    return redirect(url_for('owner.register_owner'))


