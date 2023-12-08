"""Blogly application."""

import os

from flask import Flask, redirect, render_template, request
from models import connect_db, User, Post, db


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    "DATABASE_URL", 'postgresql:///blogly')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)

# Routes


@app.get("/")
def redirect_to_users():
    # This is just the homepage so maybe index() or root()
    """Redirect to list of users"""

    return redirect(
        "/users"
        # If its a view function thats like this, it should be one line
    )


@app.get("/users")
def show_all_users():
    """
    Show all users with links to individual user pages
    Includes button to add new user
    """

    users = User.query.all()
    # order this by something just so that its not a random blob of users
    # We want the order to make sense User.query.order_by(User.first_name)


    return render_template(
        'users.html',
        users=users
    )


@app.get("/users/new")
def show_new_user_form():
    """Shows new user form"""

    return render_template(
        "/new-user.html"
        # same line for simple return statement
    )


@app.post("/users/new")
def process_new_user_form():
    """
    Process the add user form
    Adds a new user and redirects to users page
    """

    first_name = request.form["first_name"]
    last_name = request.form["last_name"]
    image_url = request.form["image_url"] or None

    user = User(first_name=first_name,
                last_name=last_name,
                image_url=image_url
            )
    # Closing paren should line up with the thing it is closing

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
    posts = Post.query.filter(Post.user_id == user_id)

    return render_template('user-detail.html',
                           user=user,
                           posts=posts
                        #    Dave says maybe put 94 on 93 (all on one line)
                           )


@app.get("/users/<int:user_id>/edit")
def show_user_edit_form(user_id):
    """
    Shows the user edit form
#   """

    user = User.query.get_or_404(user_id)

    return render_template('user-edit-page.html',
                           user=user)
# be consistent with how you are closing your parens. Pattern match pattern match!


@app.post("/users/<int:user_id>/edit")
def process_edit_form(user_id):
    """
    Process the edit form
    Returns the user to the users page
    """

    user = User.query.get(user_id)

    # change .get to .get_or_404

    first_name = request.form["first_name"]
    last_name = request.form["last_name"]
    image_url = request.form["image_url"]

    user.first_name = first_name
    user.last_name = last_name
    user.image_url = image_url

    # consolidate 121-127

    db.session.commit()

    return redirect("/users")


@app.post("/users/<int:user_id>/delete")
def delete_user(user_id):
    """
    Deletes user
    Redirects to users page
    """
    user = User.query.get(user_id)

    # .get_or_404

    db.session.delete(user)
    db.session.commit()

    return redirect("/users")

@app.get("/users/<int:user_id>/posts/new")
def show_new_post_form(user_id):
    """Shows new post form"""

    user = User.query.get(user_id)

    return render_template("/new-post.html", user = user)



@app.post("/users/<int:user_id>/posts/new")
def add_post(user_id):
    """Handle add form; add post and redirect to the user detail page."""


    post = Post(title=request.form["title"],
                content=request.form["content"],
            )
    # Closing paren should line up with the thing it is closing

    db.session.add(post)
    db.session.commit()

    return redirect(f'/users/{user_id}')


