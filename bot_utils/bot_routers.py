from aiogram import Dispatcher, Bot, types, executor

from config import TOKEN
from bot_utils.handlers import start_cmd, start_game_cmd


bot = Bot(TOKEN)
dp = Dispatcher(bot)

dp.register_message_handler(start_cmd, commands='start',)
dp.register_message_handler(start_game_cmd, commands='start_game',)

