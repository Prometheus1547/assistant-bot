import asyncio

import requests
from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext

from states import States


async def name_status(message: types.Message, state: FSMContext):
    await state.update_data(name_of_status=message.text.lower())
    await message.answer("Choose level (x/100):")
    await States.wait_for_status_estimation.set()


async def date_status(message: types.Message, state: FSMContext):
    await state.update_data(date_of_status=message.text.lower())
    status_data = await state.get_data()
    loop = asyncio.get_event_loop()
    loop.run_in_executor(None, requests.post, "https://cernev-assistant-api.herokuapp.com/api/v1/status",
                         {'estimation': status_data['date_of_status'], 'label': status_data['name_of_status']})
    await message.answer(
        f"Thank you, status: {status_data['name_of_status']}, estimation:  {status_data['date_of_status']}, is recorded")
    await state.finish()


class StatusButton:

    def __init__(self, dp: Dispatcher):
        self.dp = dp

    def init_status_button(self):
        bot = self.dp.bot

        @self.dp.callback_query_handler(lambda c: c.data == 'status')
        async def handle_action(call: types.CallbackQuery):
            await bot.answer_callback_query(call.id)
            await bot.send_message(call.from_user.id, 'Please,write the name of the status')
            await States.wait_for_status_name.set()
