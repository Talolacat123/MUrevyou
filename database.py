from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import *
from textblob import TextBlob

engine = create_engine('sqlite:///database.db?check_same_thread=False')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_album(sub_by, album_name, artist, image_link, about, why_important, stafforstudent):
	sen = TextBlob(why_important)
	polarity = sen.sentiment.polarity;
	album_obj = Album(
		album_name=album_name,
		artist = artist,
		image_link=image_link,
		about=about,
		why_important=why_important,
		sub_by = sub_by,
		stafforstudent = stafforstudent,
		sen = polarity)
	session.add(album_obj)
	session.commit()

def query_by_type(stafforstudent):
   picks = session.query(
       Album).filter_by(
       stafforstudent=stafforstudent).all()
   return picks

print(query_by_type("staff"))
print(query_by_type("student"))
