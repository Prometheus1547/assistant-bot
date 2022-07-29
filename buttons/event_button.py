import asyncio
import requests
from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from states import States
from config import HOST


async def name_event(message: types.Message, state: FSMContext):
    await state.update_data(event_name=message.text.lower())
    user_data = await state.get_data()
    loop = asyncio.get_event_loop()
    loop.run_in_executor(None, requests.post, f"{HOST}api/v1/event",
                         {'label': user_data['event_name']})
    await message.answer(f"Event {user_data['event_name']} was added")
    await state.finish()

class EventButton:
    def __init__(self, dp: Dispatcher):
        self.dp = dp
        self.bot = dp.bot

    def register_callback(self):
        bot = self.bot

        @self.dp.callback_query_handler(lambda c: c.data == 'event')
        async def handle_event(call: types.CallbackQuery):
            await bot.answer_callback_query(call.id)
            await bot.send_message(call.from_user.id, 'Please,write the name of the event')
            await States.wait_for_event_name.set()