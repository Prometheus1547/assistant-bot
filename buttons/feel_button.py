import asyncio

import requests
from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext

from states import States


async def name_feel(message: types.Message, state: FSMContext):
    await state.update_data(name_of_feel=message.text.lower())
    await message.answer("Choose estimation:")
    await States.wait_for_feel_estimation.set()


async def estimation_feel(message: types.Message, state: FSMContext):
    await state.update_data(date_of_feel=message.text.lower())
    feel_data = await state.get_data()
    loop = asyncio.get_event_loop()
    loop.run_in_executor(None, requests.post, "https://cernev-assistant-api.herokuapp.com/api/v1/feel",
                         {'category': feel_data['name_of_feel'], 'estimation': feel_data['date_of_feel']})
    await message.answer(
        f"Thank you, feel: {feel_data['name_of_feel']}, estimation:  {feel_data['date_of_feel']}, is recorded")
    await state.finish()


class FeelButton:

    def __init__(self, dp: Dispatcher):
        self.dp = dp

    def init_feel_button(self):
        bot = self.dp.bot

        @self.dp.callback_query_handler(lambda c: c.data == 'feel')
        async def handle_action(call: types.CallbackQuery):
            await bot.answer_callback_query(call.id)
            await bot.send_message(call.from_user.id, 'Please,write the name of the feel')
            await States.wait_for_feel_name.set()
