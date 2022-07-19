import asyncio
import requests
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from config import TOKEN
from markups import ikb_menu
from order import OrderFood

bot = Bot(token=TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot, storage=MemoryStorage())

async def food_start(message: types.Message):
    await message.answer("Please, choose something", reply_markup=ikb_menu)
#
#
#

def register_handlers_food(dp: Dispatcher):
    dp.register_message_handler(food_start, commands="start", state="*")

if __name__ == '__main__':
    register_handlers_food(dp)
    executor.start_polling(dp)