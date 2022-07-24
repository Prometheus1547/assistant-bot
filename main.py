import asyncio
import requests
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext

from buttons import action_button
from buttons.action_button import ActionButton
from config import TOKEN
from markups import ikb_menu
from order import Action, Feel, Status

bot = Bot(token=TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot, storage=MemoryStorage())

async def start(message: types.Message):
    await message.answer("Please, choose something", reply_markup=ikb_menu)

# ___________________________________BUTTON FEEL________________________________________
@dp.callback_query_handler(lambda c: c.data == 'feel')
async def handle_action(call: types.CallbackQuery):
    await bot.answer_callback_query(call.id)
    await bot.send_message(call.from_user.id, 'Please,write the name of the feel')
    await Feel.wait1.set()


async def name_feel(message: types.Message, state: FSMContext):
    await state.update_data(name_of_feel=message.text.lower())
    await message.answer("Choose data:")
    await Feel.wait2.set()


async def date_feel(message: types.Message, state: FSMContext):
    await state.update_data(date_of_feel=message.text.lower())
    feel_data = await state.get_data()
    loop = asyncio.get_event_loop()
    loop.run_in_executor(None, requests.post, "https://cernev-assistant-api.herokuapp.com/api/v1/feel",
                         {'category': feel_data['name_of_feel'], 'date': feel_data['date_of_feel']})
    await message.answer(
        f"Thank you, feel: {feel_data['name_of_feel']}, data:  {feel_data['date_of_feel']}, is recorded")
    await state.finish()


# ___________________________________BUTTON STATUS________________________________________
@dp.callback_query_handler(lambda c: c.data == 'status')
async def handle_action(call: types.CallbackQuery):
    await bot.answer_callback_query(call.id)
    await bot.send_message(call.from_user.id, 'Please,write the name of the status')
    await Status.wait_st1.set()


async def name_status(message: types.Message, state: FSMContext):
    await state.update_data(name_of_status=message.text.lower())
    await message.answer("Choose level (x/100):")
    await Status.wait_st2.set()


async def date_status(message: types.Message, state: FSMContext):
    await state.update_data(date_of_status=message.text.lower())
    status_data = await state.get_data()
    loop = asyncio.get_event_loop()
    loop.run_in_executor(None, requests.post, "https://cernev-assistant-api.herokuapp.com/api/v1/status",
                         {'estimation': status_data['date_of_status'], 'label': status_data['name_of_status']})
    await message.answer(
        f"Thank you, status: {status_data['name_of_status']}, estimation:  {status_data['date_of_status']}, is recorded")
    await state.finish()


def register_handlers_food(dp: Dispatcher):
    dp.register_message_handler(start, commands="start", state="*")
    dp.register_message_handler(action_button.name_action, state=Action.state_action)

    dp.register_message_handler(name_feel, state=Feel.wait1)
    dp.register_message_handler(date_feel, state=Feel.wait2)

    dp.register_message_handler(name_status, state=Status.wait_st1)
    dp.register_message_handler(date_status, state=Status.wait_st2)


if __name__ == '__main__':
    action_btn = ActionButton(dp)
    action_btn.init_action_button()
    register_handlers_food(dp)
    executor.start_polling(dp)
