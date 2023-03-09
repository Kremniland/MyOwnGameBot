import csv
import asyncio

from data_base.manager import CategoryManager


async def fill_category_data(filename: str):
    '''считывание категорий из файла и через менеджер категорий заполнение базы'''
    with open(filename, 'r', encoding='utf-8') as file:
        rows = csv.reader(file, delimiter=',')
        await CategoryManager().fill_category(rows)
    #     lst = []
    #     for row in rows:
    #         lst.append(row)
    # return lst



if __name__ == '__main__':
    asyncio.run(fill_category_data('data_files/category_data.csv'))
