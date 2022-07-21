import asyncio
import requests
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from config import TOKEN
from markups import ikb_menu
from order import OrderFood


bot = Bot(token=TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot, storage=MemoryStorage())

async def start(message: types.Message):
    await message.answer("Please, choose something", reply_markup=ikb_menu)

@dp.callback_query_handler(lambda c: c.data == 'action')
async def handle_action(call: types.CallbackQuery):
    await bot.answer_callback_query(call.id)
    await bot.send_message(call.from_user.id, 'Please,write the name of the action')
    await OrderFood.waiting_for_food_name.set()

async def name_action(message: types.Message, state: FSMContext): #Сохранили название Action в список
    await state.update_data(action_name=message.text.lower())
    user_data = await state.get_data()
    loop = asyncio.get_event_loop()
    loop.run_in_executor(None, requests.post, "https://cernev-assistant-api.herokuapp.com/api/v1/action", {'label': user_data['action_name']})
    await message.answer(f"Thank you, action: {user_data['action_name']} is recorded")
    await state.finish()




def register_handlers_food(dp: Dispatcher):
    dp.register_message_handler(start, commands="start", state="*")
    dp.register_message_handler(name_action, state=OrderFood.waiting_for_food_name)


if __name__ == '__main__':
    register_handlers_food(dp)
    executor.start_polling(dp)