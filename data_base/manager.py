import asyncio
from sqlalchemy import select, update, delete, insert
from sqlalchemy import not_
from sqlalchemy.sql import func

from data_base.db import get_session
from data_base.models import User, Category, Question, UserGuessedQuestion


class CategoryManager():
    def __init__(self):
        self.model = Category
        self.session = get_session()

    def insert_category(self, data):
        '''добавление в базу новой категории'''
        inserts = []

        for category in data: # data список категорий из csv файла
            inserts.append(
                self.model(
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


class QuestionManager():
    def __init__(self):
        self.session = get_session()
        self.model = Question

    def insert_question(self, data):
        inserts = []

        for question in data: # data список вопросов из csv файла
            inserts.append(
                self.model(
                    question=question[0],
                    answer=question[1],
                    category=question[2]
                )
            )
        self.session.add_all(inserts)
        self.session.commit()
        self.session.close()

    def get_all_question(self):
        questions = self.session.query(self.model).all()
        self.session.close()
        return questions

    def get_random_question(self, guessed_question, category_id=None):
        if category_id:
            q = self.session.query(self.model).filter(
                not_(self.model.id.in_(guessed_question)),
                self.model.category==category_id
            ).order_by(func.random()).first()
            return q
        else:
            q = self.session.query(self.model).filter(
                not_(self.model.id.in_(guessed_question))
            ).order_by(func.random()).first()
            return q


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


class GuessedQuestionManager():
    def __init__(self):
        self.model = UserGuessedQuestion
        self.session = get_session()

    def insert_guessed_question(self, user_tg_id, question_id):
        insert = self.model(
            user_tg_id=user_tg_id,
            question=question_id
        )
        self.session.add(insert)
        self.session.commit()
        self.session.close()

    def get_guessed_question(self, user_tg_id):
        results = self.session.query(self.model.question).filter(
            self.model.user_tg_id==user_tg_id
        )
        lst_ids = []
        for i in results:
            lst_ids.append(i[0])
        return lst_ids


if __name__ == '__main__':
    ids = [1,2,3]
    rand_q = QuestionManager().get_random_question(ids, 1)
    print(rand_q)
    lst = GuessedQuestionManager().get_guessed_question(1494947085)
    print(lst)
    # q = get_session().query(Question).filter(
    #     not_(Question.id.in_(ids)),
    #     Question.category == 1
    # ).order_by(func.random()).first()
    # print(q.id)

