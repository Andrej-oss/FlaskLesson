from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# from app.user.views import user
from config import DevConfig

app = Flask(__name__)
app.config.from_object(DevConfig)
# app.register_blueprint(user)

db = SQLAlchemy(app)

from app.user import views

db.create_all()
