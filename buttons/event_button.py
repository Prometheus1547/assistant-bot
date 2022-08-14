import asyncio

import requests
from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext

from commands.main_commands import start_command
from config import HOST, SLEEP_TIME
from states import States


async def name_event(message: types.Message, state: FSMContext):
    await state.update_data(event_name=message.text, user_id_from_TG=message.from_user.id)
    event_data = await state.get_data()
    loop = asyncio.get_event_loop()
    loop.run_in_executor(None, requests.post,
                         f"{HOST}api/v1/event",
                         None,
                         {'name': event_data['event_name'], 'userId': event_data['user_id_from_TG']})
    await message.answer(f"Success! Event '{event_data['event_name']}' was created.")
    await state.finish()
    await asyncio.sleep(SLEEP_TIME)
    await start_command(message)

class EventButton:
    def __init__(self, dp: Dispatcher):
        self.dp = dp
        self.bot = dp.bot

    def register_callback(self):
        bot = self.bot

        @self.dp.callback_query_handler(lambda c: c.data == 'event')
        async def handle_event(call: types.CallbackQuery):
            await bot.answer_callback_query(call.id)
            await bot.send_message(call.from_user.id, 'Please name event:')
            await States.wait_for_event_name.set()
