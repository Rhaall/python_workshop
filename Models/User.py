from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database.database import Base
from Models.KeywordByUser import KeywordByUser


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(100), unique=True, nullable=False)
    firstname = Column(String(100), nullable=False)
    lastname = Column(String(100), nullable=False)
    keyword_by_user = relationship("KeywordByUser")

    def __init__(self, username=None, firstname=None, lastname=None):
        self.username = username
        self.firstname = firstname
        self.lastname = lastname

    def __repr__(self):
        return '<User %r>' % self.username
