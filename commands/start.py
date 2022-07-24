from aiogram import types
from markups import ikb_menu


async def start(message: types.Message):
    await message.answer("Please, choose something", reply_markup=ikb_menu)
