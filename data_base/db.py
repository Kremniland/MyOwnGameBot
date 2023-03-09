from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

from config import DB_URL

engine = create_engine(DB_URL, echo=True)
Base = declarative_base()
Session = sessionmaker(autocommit=False, bind=engine, autoflush=True) # создание подключения к бд
session = Session()

def get_session():
    return session

if __name__ == '__main__':
    pass
