"""Blogly application."""

import os

from flask import Flask, redirect, render_template
from models import connect_db

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    "DATABASE_URL", 'postgresql:///blogly')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)

# Routes

@app.get("/")
def something():
    """Redirect to list of users"""


    return redirect(
        "/users/"
        # "index.html"
        # users = users
        )



@app.get("/users/")
def something():
    """
    Show all users
    All users will have a link with their name on it
    Has link to the add-user form

    """

    return render_template(
        'index.html',
        # users = users,
        # user_id = user_id,
        )

@app.get("/users/new")
def something():
    """
    Shows add form for users
    """

@app.post("/users/new")
def something():
    """
    process the add user form, adding a new user and redirects to /users
    """

@app.get("/users/int:<user_id>/")
def something():
    """
    Shows information about the given user
    Has an edit button that redirects to the edit page
    Has a delete button to delete the user

    """

@app.post("/users/int:<user_id>/edit")
def something():
    """
    show the edit page for a user
    Have a cancel button that returns to details page for a user
    Have a save button that updates the user

    """


@app.post("/users/int:<user_id>/delete")
def something():
    """
    Delete the user

    """