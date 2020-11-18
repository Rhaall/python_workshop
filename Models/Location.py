from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database.database import Base
from Models.Event import Event


class Location(Base):
    __tablename__ = 'location'
    id = Column(Integer, primary_key=True)
    city = Column(String(100), unique=True, nullable=False)
    Events = relationship("Event")

    def __init__(self, city=None):
        self.city = city

    def __repr__(self):
        return '<Location %r>' % self.city
