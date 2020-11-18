from sqlalchemy import Column, Integer, String, ForeignKey
from database.database import Base


class Event(Base):
    __tablename__ = 'event'
    id = Column(Integer, primary_key=True)
    label = Column(String(100), unique=True, nullable=False)
    location_id = Column(Integer, ForeignKey('location.id'), nullable=False)

    def __repr__(self):
        return '<Event %r>' % self.label
