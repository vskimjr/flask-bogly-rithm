from models import User, db

from app import app

db.drop_all()
db.create_all()

# In case this is run more than once, empty out existing data
User.query.delete()

# Add sample users

comedian = User(first_name = "Jerry", last_name = "Seinfeld")
comedian2 = User(first_name = "Aziz", last_name = "Ansari", image_url = 'https://media.npr.org/assets/artslife/arts/2010/02/ansari-848a3de58d46caf230f79dfa1c258be8a1f0ff50-s600-c85.webp')
comedian3 = User(first_name = "Larry", last_name = "David")

db.session.add_all([comedian, comedian2, comedian3])
db.session.commit()



