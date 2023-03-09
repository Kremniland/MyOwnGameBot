from sqlalchemy import (
    Column, Integer, String, BigInteger, UnicodeText, Text, ForeignKey
)

from data_base.db import Base, async_engine


class User(Base):
    __tablename__ = 'user'
    # __table_args__ = {'extend_existing': True}
    id = Column(Integer,
                primary_key=True,
                autoincrement=True,
                unique=True)
    user_tg_id = Column(Integer, nullable=False, unique=True)
    points = Column(Integer, default=0)


class Category(Base):
    __tablename__ = 'category'
    id = Column(Integer,
                primary_key=True,
                autoincrement=True,
                unique=True)
    name = Column(String(100), nullable=False)


class Question(Base):
    __tablename__ = 'question'
    id = Column(Integer,
                primary_key=True,
                autoincrement=True,
                unique=True)
    question = Column(Text, nullable=False)
    answer = Column(Text, nullable=False)
    category = Column(Integer, ForeignKey('category.id'), nullable=False)


async def init_models():
    '''создание моделей'''
    async with async_engine.begin() as conn:
        # await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

async def delet_models():
    '''Удаление моделей'''
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        # await conn.run_sync(Base.metadata.create_all)

if __name__ == '__main__':
    pass



