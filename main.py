import asyncio
from aiogram import executor

from bot_utils.bot_routers import dp
from utils import fill_category_data
from data_base.init_models import create_tables


if __name__ == '__main__':
    # create_tables()
    # fill_category_data('data_files/category_data.csv')
    executor.start_polling(dp,
                           skip_updates=True)

