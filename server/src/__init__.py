from flask import Flask
import os
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
from src.db import db
from flask_cors import CORS

# loading environment variables
load_dotenv()

# declaring flask application
app = Flask(__name__)

# enables CORS
CORS(app)

app.secret_key = os.environ.get('SECRET_KEY')

# Path for our local sql lite database
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("SQLALCHEMY_DATABASE_URI_DEV")

# To specify to track modifications of objects and emit signals
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = os.environ.get("SQLALCHEMY_TRACK_MODIFICATIONS")

# sql alchemy instance
db.init_app(app)

from src.models.limit import Limit
from src.models.transaction import Transaction
from src.models.user import User


# import api blueprint to register it with app
from src.routes import api
app.register_blueprint(api)
