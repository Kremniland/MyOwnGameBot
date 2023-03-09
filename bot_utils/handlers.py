from aiogram import types

from data_base.manager import UserManager
from bot_utils.keyboards import categories_ikb


async def start_cmd(message: types.Message):
    await message.answer(text='Бот запущен!')
    user_tg_id = message.from_user.id
    date = UserManager().get_user(user_tg_id)
    if date:
        score = date.points
        UserManager().update_points_user(user_tg_id=user_tg_id, points=score)
        await message.answer(f'У вас: {score} очков')
    else:
        UserManager().add_user(user_tg_id)


async def start_game_cmd(message: types.Message):
    markup = categories_ikb()
    await message.answer('Выберите категорию:',
                         reply_markup=markup)



