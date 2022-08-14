from aiogram import types

from markups import inline_markup_main


async def start_command(message: types.Message):
    await message.answer("Please choose a category:", reply_markup=inline_markup_main)
