from sqlalchemy import Column, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from database.database import Base


class KeywordByUser(Base):
    __tablename__ = 'keyword_by_user'
    id = Column(Integer, primary_key=True)
    id_user = Column(Integer, ForeignKey('user.id'), nullable=False)
    id_keyword = Column(Integer, ForeignKey('keyword.id'), nullable=False)
    pos_rate = Column(Float(), nullable=False)
    neg_rate = Column(Float(), nullable=False)
    neutral_rate = Column(Float(), nullable=False)
    count = Column(Integer, nullable=False)

    def __init__(self, username=None, id_user=None, id_keyword=None, pos_rate=None, neg_rate=None, neutral_rate=None, count=None):
        self.username = username
        self.id = id
        self.id_user = id_user
        self.id_keyword = id_keyword
        self.pos_rate = pos_rate
        self.neg_rate = neg_rate
        self.neutral_rate = neutral_rate
        self.count = count

    def __repr__(self):
        return '<KeywordByUser %r>' % self.username
