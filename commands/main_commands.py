from aiogram import types
from markups import inline_markup_main


async def start(message: types.Message):
    await message.answer("Please, choose something", reply_markup=inline_markup_main)
