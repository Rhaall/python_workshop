from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database.database import Base
from Models.KeywordByUser import KeywordByUser


class Keyword(Base):
    __tablename__ = 'keyword'
    id = Column(Integer, primary_key=True)
    label = Column(String(100), unique=True, nullable=False)
    keyword_by_user = relationship("KeywordByUser")

    def __init__(self, label=None):
        self.label = label

    def __repr__(self):
        return '<Keyword %r>' % self.label
