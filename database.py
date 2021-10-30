from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import *

engine = create_engine('sqlite:///database.db?check_same_thread=False')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

# ------------Functions---------------
#def add_user(username, email, bio):
#	user_obj = User(
#		username=username,
#		email=email,
#		bio=bio)
#	session.add(user_obj)
#	session.commit()
#	print("added " + username)

def add_album(sub_by, album_name, artist, image_link, about, why_important, stafforstudent):
	album_obj = Album(
		album_name=album_name,
		artist = artist,
		image_link=image_link,
		about=about,
		why_important=why_important,
		sub_by = sub_by,
		stafforstudent = stafforstudent)
	session.add(album_obj)
	session.commit()
#	print(image_link + album_name +"by "+ album_name + "submitted by: " + sub_by + "about: " + about + "" + "Why its important to me: " + why_important)

def query_by_type(stafforstudent):
   picks = session.query(
       Album).filter_by(
       stafforstudent=stafforstudent).all()
   return picks

#def query_all():
#   """
#   Print all the students
#   in the database.
#   """
#   albums = session.query(
#      Album).all()
#   return albums

#print (query_all())
print(query_by_type("staff"))
print(query_by_type("student"))