from sqlalchemy import Column, Integer, String, ForeignKey
from database.database import Base
from sqlalchemy.orm import relationship
from Models.Keyword import Keyword


class Event(Base):
    __tablename__ = 'event'
    id = Column(Integer, primary_key=True)
    label = Column(String(100), unique=True, nullable=False)
    description = Column(String(2000), nullable=False)
    picture = Column(String(255), nullable=False)
    location_id = Column(Integer, ForeignKey('location.id'), nullable=False)
    Keyword = relationship("Keyword")

    def __repr__(self):
        return '<Event %r>' % self.label
