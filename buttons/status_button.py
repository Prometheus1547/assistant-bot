import asyncio

import requests
from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove

from config import HOST
from markups import keyboard_for_estimation
from states import States


async def name_status(message: types.Message, state: FSMContext):
    await state.update_data(name_of_status=message.text)
    await message.answer("Please estimate:", reply_markup=keyboard_for_estimation)
    await States.wait_for_status_estimation.set()


async def estimation_status(message: types.Message, state: FSMContext):
    await state.update_data(estimation_of_status=message.text, user_id_from_TG=message.from_user.id)
    if message.text.isdigit():
        status_data = await state.get_data()
        loop = asyncio.get_event_loop()
        loop.run_in_executor(None, requests.post, f"{HOST}api/v1/status",
                             {'estimation': status_data['estimation_of_status'],
                              'userId': status_data['user_id_from_TG'], 'name': status_data['name_of_status']})
        await message.answer(
            f"Success! Status '{status_data['name_of_status']}', estimation '{status_data['estimation_of_status']}' was created.",
            reply_markup=ReplyKeyboardRemove())
        await state.finish()
    else:
        await message.answer("Sorry! Please give the estimation:")


class StatusButton:

    def __init__(self, dp: Dispatcher):
        self.dp = dp

    def register_callback(self):
        bot = self.dp.bot

        @self.dp.callback_query_handler(lambda c: c.data == 'status')
        async def handle_action(call: types.CallbackQuery):
            await bot.answer_callback_query(call.id)
            await bot.send_message(call.from_user.id, 'Please name status:')
            await States.wait_for_status_name.set()
