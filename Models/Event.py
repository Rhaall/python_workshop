from sqlalchemy import Column, Integer, String, ForeignKey, Text
from database.database import Base
from sqlalchemy.orm import relationship
from Models.Keyword import Keyword


class Event(Base):
    __tablename__ = 'event'
    id = Column(Integer, primary_key=True)
    label = Column(String(100), unique=True, nullable=False)
    title = Column(Text(), nullable=False)
    description = Column(Text(), nullable=False)
    company_name = Column(String(100), nullable=False)
    price = Column(String(100), nullable=False)
    date = Column(String(100), nullable=False)
    duration = Column(String(100), nullable=False)
    address = Column(String(100), nullable=False)
    zipcode = Column(String(100), nullable=False)
    picture1 = Column(String(255), nullable=False)
    picture2 = Column(String(255), nullable=False)
    picture3 = Column(String(255), nullable=False)
    location_id = Column(Integer, ForeignKey('location.id'), nullable=False)
    Keyword = relationship("Keyword")

    def __repr__(self):
        return '<Event %r>' % self.label
