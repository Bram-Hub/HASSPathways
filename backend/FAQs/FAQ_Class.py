from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Faqs(Base):
    __tablename__ = 'FAQs'
    id = Column(Integer, primary_key=True, autoincrement=True)
    # 指定name映射到name字段; name字段为字符串类形，
    Question = Column(String())
    Answer = Column(String())

    def __repr__(self):
        return "<FAQs(Question = '%s', Answer = '%s')>" % (
            self.Question, self.Answer)
