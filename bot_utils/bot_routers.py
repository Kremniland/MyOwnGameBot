from aiogram import Dispatcher, Bot

from config import TOKEN
from bot_utils.handlers import start_cmd, start_game_cmd, select_category, finish_game, send_answer


bot = Bot(TOKEN)
dp = Dispatcher(bot)


dp.register_message_handler(finish_game, commands='stop_game',)
dp.register_message_handler(start_cmd, commands='start',)
dp.register_message_handler(start_game_cmd, commands='start_game',)
dp.register_message_handler(send_answer)


dp.register_callback_query_handler(select_category, lambda c: c.data.startswith('category_'))


