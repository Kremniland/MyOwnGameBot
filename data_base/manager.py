import asyncio
from sqlalchemy import select, update, delete, insert

from data_base.db import get_session
from data_base.models import User, Category


class CategoryManager():
    def __init__(self):
        self.model = Category
        self.session = get_session()

    def insert_category(self, data):
        '''добавление в базу новой категории'''
        inserts = []

        for category in data: # data список категорий из csv файла
            inserts.append(
                Category(
                    name=category[0]
                )
            )
        self.session.add_all(inserts)
        self.session.commit()
        self.session.close()

    def get_all_categories(self):
        '''получение всех категорий из базы'''
        results = self.session.query(self.model).all()
        self.session.close()
        return results


class UserManager:
    def __init__(self):
        self.session = get_session()
        self.model = User

    def add_user(self, user_tg_id: int, points: int = 0):

        user = self.model(user_tg_id=user_tg_id, points=points)
        self.session.add(user)
        self.session.commit()
        self.session.close()

    def get_user(self, user_tg_id: int):
        user = self.session.query(self.model).filter(User.user_tg_id==user_tg_id).first()
        self.session.close()
        return user

    def update_points_user(self, user_tg_id: int, points: int):
        user = self.session.query(self.model).filter(self.model.user_tg_id == user_tg_id).first()
        user.points = points
        self.session.add(user)
        self.session.commit()
        self.session.close()



if __name__ == '__main__':
    user = UserManager().add_user(12345678, 1000)
    print(user)

