from flask import Flask

from app.user.views import user
from config import DevConfig

app = Flask(__name__)
app.config.from_object(DevConfig)
app.register_blueprint(user)

from app import view
