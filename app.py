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
        "/users"
    )


@app.get("/users")
def show_all_users():
    """
    Show all users with links to individual user pages
    Includes button to add new user
    """

    users = User.query.all()

    return render_template(
        'users.html',
        users=users
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
    Process the add user form
    Adds a new user and redirects to users page
    """

    first_name = request.form["first_name"]
    last_name = request.form["last_name"]
    image_url = request.form["image_url"]

    user = User(first_name=first_name,
                last_name=last_name,
                image_url=image_url
                )

    db.session.add(user)
    db.session.commit()

    return redirect("/users")


@app.get("/users/<int:user_id>/")
def show_user_profile_page(user_id):
    """
    Shows information about the given user
    Has an edit button that redirects to the edit page
    Has a delete button to delete the user
    """

    user = User.query.get_or_404(user_id)

    return render_template('user-detail.html',
                           user=user
                           )


@app.get("/users/<int:user_id>/edit")
def show_user_edit_form(user_id):
    """
    Shows the user edit form
#   """

    user = User.query.get_or_404(user_id)

    return render_template('user-edit-page.html',
                           user=user)


@app.post("/users/<int:user_id>/edit")
def process_edit_form(user_id):
    """
    Process the edit form
    Returns the user to the users page
    """

    user = User.query.get(user_id)

    first_name = request.form["first_name"]
    last_name = request.form["last_name"]
    image_url = request.form["image_url"]

    user.first_name = first_name
    user.last_name = last_name
    user.image_url = image_url

    db.session.commit()

    return redirect("/users")


@app.post("/users/<int:user_id>/delete")
def delete_user(user_id):
    """
    Deletes user
    Redirects to users page
    """
    user = User.query.get(user_id)

    db.session.delete(user)
    db.session.commit()

    return redirect("/users")
