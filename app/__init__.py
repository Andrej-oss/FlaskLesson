from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# from app.user.views import user
from config import DevConfig

app = Flask(__name__)
app.config.from_object(DevConfig)
# app.register_blueprint(user)

db = SQLAlchemy(app)

from app import view
from app.owner import models
from app.owner.views import owner

app.register_blueprint(owner)

db.create_all()
