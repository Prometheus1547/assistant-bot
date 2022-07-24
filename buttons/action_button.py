import asyncio
import requests
from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from states import States
from config import HOST




async def name_action(message: types.Message, state: FSMContext):
    await state.update_data(action_name=message.text.lower())
    user_data = await state.get_data()
    loop = asyncio.get_event_loop()
    loop.run_in_executor(None, requests.post, f"{HOST}api/v1/action",
                         {'label': user_data['action_name']})
    await message.answer(f"Thank you, action: {user_data['action_name']} is recorded")
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
            await bot.send_message(call.from_user.id, 'Please,write the name of the action')
            await States.wait_for_action_name.set()
