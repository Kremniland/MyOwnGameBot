import asyncio
from models import init_models, delet_models

def create_table():
    '''создание моделей'''
    asyncio.run(init_models())


def drop_table():
    '''удаление моделей'''
    asyncio.run(delet_models())


if __name__ == '__main__':
    create_table()


