"""Blogly application."""

import os

from flask import Flask, redirect, render_template, request
from models import connect_db, User, db


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    "DATABASE_URL", 'postgresql:///blogly')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)

# Routes

@app.get("/")
def redirect_to_users():
    """Redirect to list of users"""

    return redirect(
        "/users/"
        )


@app.get("/users/")
def show_all_users():
    """
    Show all users
    All users will have a link with their name on it
    Has link to the new-user form
    """

    users = User.query.all()

    return render_template(
        'users.html',
        users = users
        
        # [<User 1>, <User 2>, <User 3>]
        # user_id = user_id, <- add this to HTML eventually as all users need a link
        )


@app.get("/users/new")
def show_new_user_form():
    """Shows new user form"""

    return render_template(
        "/new-user.html"
        )

@app.post("/users/new")
def process_new_user_form():
    """
    process the add user form, adding a new user and redirects to /users
    """

    first_name = request.form["first_name"]
    last_name = request.form["last_name"]
    image_URL = request.form["image_URL"]

    user = User(first_name = first_name,
                last_name = last_name,
                image_URL = image_URL
                )

    db.session.add(user)
    db.session.commit()

    return redirect('/users')

# @app.get("/users/int:<user_id>/")
# def something():
#     """
#     Shows information about the given user
#     Has an edit button that redirects to the edit page
#     Has a delete button to delete the user

#     """

# @app.post("/users/int:<user_id>/edit")
# def something():
#     """
#     show the edit page for a user
#     Have a cancel button that returns to details page for a user
#     Have a save button that updates the user

#     """


# @app.post("/users/int:<user_id>/delete")
# def something():
#     """
#     Delete the user

#     """