import asyncio
from sqlalchemy import select, update, delete, insert

from data_base.db import async_session
from data_base.models import User, Category


class CategoryManager:
    def __init__(self):
        self.session = async_session()
        self.model = Category

    async def fill_category(self, data):
        '''заполнение категорий через ф-ию считывающую список категорий из файла из файла'''
        inserts = []
        async with self.session as session:
            for category in data:
                inserts.append(
                    Category(
                        name=category[0],
                    )
                )
            session.add_all(inserts)
            await session.commit()
            await session.close()

    async def get_all_category(self):
        async with self.session as session:
            result = await session.execute(select(self.model))
            await session.commit()
            await session.close()
            return result.scalars()


class UserManager:
    def __init__(self):
        self.session = async_session()
        self.model = User

    async def add_user(self, id: int, points: int = 0):
        async with self.session as session:
            user = self.model(user_tg_id=id, points=points)
            session.add(user)
            await session.commit()
            await session.close()

    async def get_user(self, user_tg_id: int):
        async with self.session as session:
            user = await session.execute(select(self.model).where(self.model.user_tg_id==user_tg_id))
            await session.commit()
            await session.close()
        return user.scalars().first()

    async def update_points_user(self, user_tg_id: int, points: int):
        async with async_session() as session:
            await session.execute(update(self.model).where(self.model.user_tg_id == user_tg_id).values(points=points))
            await session.commit()
            await session.close()



if __name__ == '__main__':
    user = UserManager()
    asyncio.run(user.add_user(1111, 123))

