from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import declarative_base

Base = declarative_base()

# --------------Tables------------------
#class User(Base):
#   __tablename__ = 'users'
#   id = Column(Integer, primary_key=True)
#   name = Column(String)
#   photo = Column(String)
#   stafforstudent = Column(Boolean)

class Album(Base):
   __tablename__ = 'albums'
   id = Column(Integer, primary_key=True)
   sub_by = Column(String)
   album_name = Column(String)
   artist = Column(String)
   image_link = Column(String)
   about = Column(String)
   why_important = Column(String)
   stafforstudent = Column(String)