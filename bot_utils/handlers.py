from aiogram import types

from data_base.manager import UserManager, GuessedQuestionManager,QuestionManager
from bot_utils.keyboards import categories_ikb
from redis_client import redis_client


def get_random_question(user_tg_id, category):
    guessed_questions = GuessedQuestionManager().get_guessed_question(user_tg_id)
    result = QuestionManager().get_random_question(guessed_questions, category)
    return result


async def start_cmd(message: types.Message):
    user_date = UserManager().get_user(message.from_user.id)
    if not user_date: # если юзера нет в базе то добавляем
        UserManager().add_user(user_tg_id=message.from_user.id)
    text = '''
        Бот запущен!
        Для начала игры напишите /start_game
    '''
    await message.answer(text=text)


async def start_game_cmd(message: types.Message):
    '''старт игры вывод инлайн клавитуры для выбора категорий'''
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


async def select_category(callback: types.CallbackQuery):
    '''Выбор категории и отображение рандомного вопроса, добавление данных
    в редис с выбранной категорией и раданные по рандомному вопросу'''
    user_data = redis_client.get_user_date(callback.from_user.id)
    if user_data:
        text = 'У вас не завершена игра завершите прежде чем начать новую'
        await callback.message.answer(text=text)
    else:
        choice = int(str(callback.data).split('_')[1]) # ИД выбранной категории
        data = {
            'category_choice': choice,
        }
        user_tg_id = callback.from_user.id
        redis_client.cache_user_data(user_tg_id, data) # помещаем в редис номер выбранной категории
        question = get_random_question(user_tg_id, choice) # получаем рандомный вопрос
        # сохраняем данные по рандомному вопросу в редис
        redis_client.cache_user_data(user_tg_id=user_tg_id, data={'id': question.id, 'question': question.question, 'answer': question.answer})
        await callback.message.answer('Вы выбрали категорию. Игра началась...')
        await callback.message.answer(f'{question.question} ?')


async def send_answer(message: types.Message):
    user_tg_id = message.from_user.id
    user_data = redis_client.get_user_date(user_tg_id)
    if user_data:
        answer = message.text # берем ответ пользователя из сообщения
        user_question = redis_client.get_user_date(user_tg_id) # берем данные игрока из редис
        answer_redis = user_data[b'answer'].decode('utf-8') # берем правильный ответ на заданный вопрос из редис
        print(answer_redis)
        if answer.lower() == answer_redis.lower():
            await message.answer('Угадали!!!!!!!!!')
            id_guessed_question = int(user_data[b'id'].decode('utf-8'))
            print(id_guessed_question)
            # добавляем отгаданный пользователем вопрос в базу
            GuessedQuestionManager().insert_guessed_question(user_tg_id, id_guessed_question)
            redis_client.del_user_data(user_tg_id) # удаляем данные пльзователя из редис
            # добавляем юзеру очков и сохраняем в базе
            user = UserManager().get_user(user_tg_id)
            score = user.points + 100
            UserManager().update_points_user(user_tg_id, score)
        else:
            await message.answer('Не угадали! еще раз попробуйте')
    else:
        text = 'У вас нет активной игры запустите начало игры'
        await message.answer(text=text)


async def finish_game(message: types.Message):
    '''окончание игры удаление данных из редис'''
    user_tg_id = message.from_user.id
    user = UserManager().get_user(user_tg_id)
    redis_client.del_user_data(user_tg_id=user_tg_id)
    await message.answer('Игра остановлена!')
    await message.answer(f'Колличество очков у вас: {user.points}')




