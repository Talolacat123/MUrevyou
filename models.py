from sqlalchemy import Column, Integer, String, Boolean, Float
from sqlalchemy.orm import declarative_base

Base = declarative_base()

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
   sen = Column(Float)
