from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Faqs(Base):
    __tablename__ = 'questions'
    Question = Column(String(), primary_key=True, unique=True)
    Answer = Column(String())

    def __int__(self, Question, Answer):
        self.Question = Question
        self.Answer = Answer

    def __repr__(self):
        return "<FAQs(Question = '%s', Answer = '%s')>" % (
            self.Question, self.Answer)
