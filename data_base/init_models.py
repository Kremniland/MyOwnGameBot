from data_base.db import Base, engine


def create_tables():
    '''создает все таблицы в базе'''
    Base.metadata.create_all(engine, checkfirst=True) # создаст все таблицы созданные на основе Base
                                                    # checkfirst=True - проверяет есть ли таблицы


if __name__ == '__main__':
    create_tables()


