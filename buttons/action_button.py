import asyncio

import requests
from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext

from config import HOST
from states import States


async def name_action(message: types.Message, state: FSMContext):
    await state.update_data(action_name=message.text, user_id_from_TG=message.from_user.id)
    action_data = await state.get_data()
    loop = asyncio.get_event_loop()
    loop.run_in_executor(None,
                         requests.post,
                         f"{HOST}api/v1/action",
                         None,
                         {'name': action_data['action_name'], 'userId': action_data['user_id_from_TG']})
    await message.answer(f"Success! Action '{action_data['action_name']}' was created.")
    await state.finish()


class ActionButton:
    def __init__(self, dp: Dispatcher):
        self.dp = dp
        self.bot = dp.bot

    def register_callback(self):
        bot = self.bot

        @self.dp.callback_query_handler(lambda c: c.data == 'action')
        async def handle_action(call: types.CallbackQuery):
            await bot.answer_callback_query(call.id)
            await bot.send_message(call.from_user.id, 'Please name action:')
            await States.wait_for_action_name.set()
