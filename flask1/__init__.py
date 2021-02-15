from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import os
import dotenv

app = Flask(__name__)
dotenv.load_dotenv(dotenv.find_dotenv()) 
app.config["SECRET_KEY"] = os.environ.get("FLASK_SECRET")
app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

from flask1 import routes 
