import csv

from data_base.manager import CategoryManager, QuestionManager


def fill_category_data(filename):
    '''заполняем данные в категории из csv файл'''
    with open(filename, 'r', encoding='utf-8') as csv_file:
        rows = csv.reader(csv_file, delimiter=',')
        # for i in rows:
        #     print(i)
        CategoryManager().insert_category(rows)


def fill_question_data(filename):
    '''заполняем данные в модель фильмы'''
    with open(filename, 'r', encoding='utf-8') as csv_file:
        rows = csv.reader(csv_file, delimiter=',')
        # for i in rows:
        #     print(i)
        QuestionManager().insert_question(rows)


if __name__ == '__main__':
    fill_category_data('data_files/category_data.csv')
    fill_question_data('data_files/question_data.csv')



