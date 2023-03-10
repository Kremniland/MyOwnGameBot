from aiogram import types

from data_base.manager import CategoryManager


def categories_ikb():
    categories = CategoryManager().get_all_categories()
    markup = types.InlineKeyboardMarkup(width=1)
    for category in categories:
        markup.add(types.InlineKeyboardButton(category.name, callback_data=f'category_{category.id}'))
    # markup.add(types.InlineKeyboardButton('Смешанные вопросы', callback_data=f'category_all'))
    return markup

if __name__ == '__main__':
    pass

