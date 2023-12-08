from models import DEFAULT_IMAGE_URL, User
from app import app, db
from unittest import TestCase
import os

os.environ["DATABASE_URL"] = "postgresql:///blogly_test"


# Make Flask errors be real errors, rather than HTML pages with error info
app.config['TESTING'] = True

# This is a bit of hack, but don't use Flask DebugToolbar
app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']

# Create our tables (we do this here, so we only create the tables
# once for all tests --- in each test, we'll delete the data
# and create fresh new clean test data

db.drop_all()
db.create_all()


class UserViewTestCase(TestCase):
    """Test views for users."""

    def setUp(self):
        """Create test client, add sample data."""

        # As you add more models later in the exercise, you'll want to delete
        # all of their records before each test just as we're doing with the
        # User model below.
        User.query.delete()

        test_user = User(
            first_name="test1_first",
            last_name="test1_last",
            image_url=None,
        )

        db.session.add(test_user)
        db.session.commit()

        # We can hold onto our test_user's id by attaching it to self (which is
        # accessible throughout this test class). This way, we'll be able to
        # rely on this user in our tests without needing to know the numeric
        # value of their id, since it will change each time our tests are run.
        self.user_id = test_user.id

    def tearDown(self):
        """Clean up any fouled transaction."""
        db.session.rollback()

    def test_list_users(self):
        """
        Tests to see if users appear on users page
        by testing if test_user appears on users page
        """

        with app.test_client() as c:
            resp = c.get("/users")
            self.assertEqual(resp.status_code, 200)
            html = resp.get_data(as_text=True)
            self.assertIn("test1_first", html)
            self.assertIn("test1_last", html)

    def test_redirect_to_users(self):
        """
        Tests if "/" correctly redirects to "/users"
        """

        with app.test_client() as c:
            response = c.get("/")
            self.assertEqual(response.status_code, 302)
            self.assertEqual(response.location, "/users")

    def test_show_new_user_form(self):
        """
        Tests if new user form renders
        """

        with app.test_client() as c:
            response = c.get('/users/new')
            html = response.get_data(as_text=True)
            self.assertIn('<input type="submit" value="Add"', html)
            # maybe look for something unique. Put a comment in /users/new html and then look for this comment
            self.assertEqual(response.status_code, 200)

    def test_process_edit_form(self):
        """
        Test if edit user form properly processes edited user information
        """

        with app.test_client() as c:
            response = c.post(
                f'/users/{self.user_id}/edit',
                data={'first_name': 'Slim',
                      'last_name': 'Charles',
                      'image_url': 'https://static.wikia.nocookie.net/thewire/images/9/93/Slim_Charles.jpg/revision/latest?cb=20200316063003'},
                follow_redirects=True)

            html = response.get_data(as_text=True)

            self.assertEqual(response.status_code, 200)
            self.assertIn('Slim', html)

            # add a few more asserts. See if 'Charles' is there
            # Test adding. We tested editing. We should test for add if we give image, not give an image, etc ***

            # Add test for /users/id is it showing the correct user?

            # Test delete
