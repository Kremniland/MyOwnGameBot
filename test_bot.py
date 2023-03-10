import asyncio
from aiogram import executor

from bot_utils.bot_routers import dp

from aiogram import types

from data_base.manager import UserManager, GuessedQuestionManager,QuestionManager
from bot_utils.keyboards import categories_ikb
from redis_client import redis_client



def get_random_question(user_tg_id, category):
    guessed_questions = GuessedQuestionManager().get_guessed_question(user_tg_id)
    result = QuestionManager().get_random_question(guessed_questions, category)
    return result


async def start_cmd(message: types.Message):
    text = '''
        Бот запущен!
        Для начала игры напишите /start_game
    '''
    await message.answer(text=text)


async def start_game_cmd(message: types.Message):
    user_tg_id = message.from_user.id
    user_data = redis_client.get_user_date(user_tg_id)
    if user_data:
        text = 'У вас уже есть запущенная игра. Желаете завершить? /stop_game'
        await message.answer(text=text)
    else:
        text = 'выберете категорию:'
        markup = categories_ikb()
        await message.answer(text=text,
                         reply_markup=markup)


async def start_category(callback: types.CallbackQuery):
    print(callback.data)
    user_data = redis_client.get_user_date(callback.from_user.id)
    if user_data:
        text = 'У вас не завершена игра завершите прежде чем начать новую'
        await callback.message.answer(text=text)
    else:
        choice = str(callback.data).split('_')[1]
        data = {
            'category_choice': choice,
        }
        user_tg_id = callback.from_user.id
        redis_client.cache_user_data(user_tg_id, data)
        question = get_random_question(user_tg_id, choice)
        redis_client.cache_user_data(user_tg_id=user_tg_id, data={'id': question.id, 'question': question.question, 'answer': question.answer})
        await callback.message.answer('Вы выбрали категорию. Игра началась...')
        await callback.message.answer(f'{question.question} ?')


async def finish_game(message: types.Message):
    '''окончание игры удаление данных из редис'''
    user_id = message.from_user.id
    redis_client.delete_user_data(user_id)
    await message.answer('Игра удалена!')
    await message.answer('Колличество угаданных фильмов: 0')




if __name__ == '__main__':

    executor.start_polling(dp,
                           skip_updates=True)
