import asyncio

from sqlalchemy import (
    Column, Integer, String, BigInteger, UnicodeText, Text, ForeignKey, Float
)
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy import select, update, insert, delete

from config import ASYNC_DB_URL
from data_base.db import async_session
from data_base.models import User


async def add_user(id: int, points: int = 0):
    async with async_session() as session:
        user = User(user_tg_id=id, points=points)
        session.add(user)
        await session.commit()
        await session.close()


async def get_user(user_tg_id):
    async with async_session() as session:
        user = await session.execute(select(User).where(User.user_tg_id == user_tg_id))
        await session.commit()
        await session.close()
    return user.scalars()


async def update_points_user(user_tg_id, points):
    async with async_session() as session:
        await session.execute(update(User).where(User.user_tg_id == user_tg_id).values(points=points))
        await session.commit()
        # await session.close()




if __name__ == '__main__':
    a1 = asyncio.run(get_user(1234567))
    print(a1.__dict__)
    # asyncio.run(update_points_user(1234567, 200))
    pass

