from models import User, db

from app import app

db.drop_all()
db.create_all()


comedian = User(first_name = "Jerry", last_name = "Seinfeld")

db.session.add_all([comedian])
db.session.commit()



