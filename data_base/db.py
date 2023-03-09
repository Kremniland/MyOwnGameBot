import asyncio

from sqlalchemy import (
    Column, Integer, String, BigInteger, UnicodeText, Text, ForeignKey, Float
)
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy import select

from config import ASYNC_DB_URL

Base = declarative_base()

async_engine = create_async_engine(
    ASYNC_DB_URL,
    echo=True,
)

async_session = sessionmaker(async_engine, expire_on_commit=False, class_=AsyncSession)


if __name__ == '__main__':
    pass
