from datetime import datetime

from sqlalchemy import create_engine, Column, Integer, String, Float, Text, DateTime, ForeignKey, Table
from sqlalchemy.orm import scoped_session, sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///answers_lion_db.db')

db_session = scoped_session(sessionmaker(bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()


class AnswersTimer(Base):
    __tablename__ = 'answers_timer'
    id = Column(Integer, primary_key=True)
    content = Column(String(150), unique=True)

    def __init__(self, content=None):
        self.content = content



class AnswersLion(Base):
    __tablename__ = 'answers_lion'
    id = Column(Integer, primary_key=True)
    content = Column(String(150), unique=True)

    def __init__(self, content=None):
        self.content = content
        
class AnswersAnother(Base):
    __tablename__ = 'answers_another'
    id = Column(Integer, primary_key=True)
    content = Column(String(150), unique=True)

    def __init__(self, content=None):
        self.content = content

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(50))
    last_name = Column(String(50))
    id_user_chat = Column(String(120), unique=True)

    def __init__(self, first_name=None, last_name=None, id_user_chat=None):
        self.first_name = first_name
        self.last_name = last_name
        self.id_user_chat = id_user_chat


if __name__ == "__main__":
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    # добавляем валюту
    #coin = CoinBase(coin_name='coin1', price_usd='12', query_date=datetime.now())
    # и пользователя (пока они не связаны)
    #user = UserQuery(user_id="123456")
    # теперь пользователю добавим валюту
    #user.coins = [coin]
    #db_session.add(user)
    #db_session.commit()
    #coin_link = db_session.query(UserCoin).filter(UserQuery.id == user.id, CoinBase.id == coin.id).first()
    #coin_link.query_minmax = '1222'
    #db_session.add(coin_link)
    #db_session.commit()