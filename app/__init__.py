from flask import Flask
from config import Config
from flask_bootstrap import Bootstrap
from flask_mail import Mail

app = Flask(__name__)

app.config.from_object(Config)

bootstrap = Bootstrap(app)
mail = Mail(app)

app.static_folder = 'static'

from app import routes