from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
import datetime


Base = declarative_base() # Базовый класс для всех моделей, используется для создания классов
                          # Представляет таблицы базы данных


# Создаем модели

class Questionnaire(Base):
    __tablename__ = 'Questionnaire'
    id = Column(Integer, primary_key=True, autoincrement=True)
    created_on = Column(DateTime, default=datetime.datetime.now)
    modified_on = Column(DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now)
    name = Column(String, nullable=False)

    questions = relationship('Question', back_populates='questionnaire') # Связь с моделью Question


class Question(Base):
    __tablename__ = 'Question'
    id = Column(Integer, primary_key=True, autoincrement=True)
    type = Column(Integer, nullable=False)
    questionnaire_id = Column(Integer, ForeignKey('Questionnaire.id'))
    order = Column(Integer, nullable=False)
    name = Column(String, nullable=False)

    questionnaire = relationship('Questionnaire', back_populates='question') # Связь с моделью Questionnaire
    answers = relationship('QuestionAnswer', back_populates='question') # Связь с моделью QuestionAnswer



class QuestionAnswer(Base):
    __tablename__ = 'QuestionAnswer'
    id = Column(Integer, primary_key=True, autoincrement=True)
    question_id = Column(Integer, ForeignKey('Question.id'))
    order = Column(Integer, nullable=False)
    name = Column(String, nullable=False)

    question = relationship('Question', back_populates='answer')


