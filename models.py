"""Models for Blogly."""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

db = SQLAlchemy()

DEFAULT_IMAGE_URL = 'https://upload.wikimedia.org/wikipedia/en/thumb/2/25/New_York_Knicks_logo.svg/800px-New_York_Knicks_logo.svg.png'

def connect_db(app):
    """Connect to database."""
    app.app_context().push()
    db.app = app
    db.init_app(app)

# Model definitions

class User(db.Model):
    """User for Blogly"""

    __tablename__ = "users"

    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True
    )

    first_name = db.Column(
        db.Text,
        nullable=False
    )

    last_name = db.Column(
        db.Text,
        nullable=False
    )

    image_url = db.Column(
        db.Text,
        nullable=True,
        default=DEFAULT_IMAGE_URL
    )

    # .String is used for stuff like first_name and stuff 
    # db.Text is more for longform stuff like "give us comments on how our food is"
