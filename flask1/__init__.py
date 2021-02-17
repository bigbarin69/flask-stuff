from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import os
import dotenv
import requests

class CustomFlask(Flask):
    """Override default `run` method, to also send a message in Discord when the site is deployed on heroku."""
    def run(self, host=None, port=None, debug=None, load_dotenv=True, **options):
        webhook = os.environ.get("WEBHOOK_URL")
        # WEBHOOK_URL is added as a config var on heroku
        # So what happens is:
        # if site is being run on heroku, the config var exists (it won't be None)
        if webhook is not None:
            # in this case, we send a message to the git-updates discord channel
            # ignore, this is just stuff to send message
            embed = {"title": "Preo site is online!", "url": "https://preo-flask-app.herokuapp.com", "color": 5814783}
            json = {"username": "preo", "avatar_url": "https://images-ext-1.discordapp.net/external/OZ1OJNdjcLZG8LgFMunuPjacQKjUMACflNzXCw1DKsw/https/cdn.discordapp.com/avatars/293705095059734528/82730b20ec777dbb6630ea4bed9805e6.png?width=96&height=96"}
            json["embeds"] = [embed]
            requests.post(webhook, json=json)
            
        # now that we've sent the message, start the server the same way as before
        super().run(host=host, port=port, debug=debug, load_dotenv=load_dotenv, **options)


# Now instead of using normal Flask, use the custom version
app = CustomFlask(__name__)

dotenv.load_dotenv(dotenv.find_dotenv())

app.config["SECRET_KEY"] = os.environ.get("FLASK_SECRET")
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DATABASE_URL")

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

from flask1 import routes 
