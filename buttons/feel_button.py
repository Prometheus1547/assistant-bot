import asyncio
import requests
from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from states import States
from config import HOST


async def name_feel(message: types.Message, state: FSMContext):
    await state.update_data(name_of_feel=message.text.lower())
    await message.answer("Please give the estimation:")
    await States.wait_for_feel_estimation.set()


async def estimation_feel(message: types.Message, state: FSMContext):
    await state.update_data(estimation_of_feel=message.text.lower(), user_id_from_TG= message.from_user.id)
    feel_data = await state.get_data()
    loop = asyncio.get_event_loop()
    loop.run_in_executor(None, requests.post, f"{HOST}api/v1/feel",
                         {'category': feel_data['name_of_feel'], 'userId': feel_data['user_id_from_TG'], 'estimation': feel_data['estimation_of_feel']})
    await message.answer(
        f"Success! Feel '{feel_data['name_of_feel']}' with estimation of '{feel_data['estimation_of_feel']}' was created.")
    await state.finish()


class FeelButton:

    def __init__(self, dp: Dispatcher):
        self.dp = dp

    def register_callback(self):
        bot = self.dp.bot

        @self.dp.callback_query_handler(lambda c: c.data == 'feel')
        async def handle_action(call: types.CallbackQuery):
            await bot.answer_callback_query(call.id)
            await bot.send_message(call.from_user.id, 'Please,write the name of the feel')
            await States.wait_for_feel_name.set()
