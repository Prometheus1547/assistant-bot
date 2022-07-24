from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from config import TOKEN
from handlers.main_handler import register_buttons, register_handlers

bot = Bot(token=TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot, storage=MemoryStorage())

if __name__ == '__main__':
    register_buttons(dp)
    register_handlers(dp)
    executor.start_polling(dp)
