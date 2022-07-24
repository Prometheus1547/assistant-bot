from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from buttons import action_button, feel_button, status_button
from buttons.action_button import ActionButton
from buttons.feel_button import FeelButton
from buttons.status_button import StatusButton
from config import TOKEN
from markups import ikb_menu
from order import Action, Feel, Status

bot = Bot(token=TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot, storage=MemoryStorage())


async def start(message: types.Message):
    await message.answer("Please, choose something", reply_markup=ikb_menu)


def register_handlers_food(dp: Dispatcher):
    dp.register_message_handler(start, commands="start", state="*")
    dp.register_message_handler(action_button.name_action, state=Action.state_action)

    dp.register_message_handler(feel_button.name_feel, state=Feel.wait1)
    dp.register_message_handler(feel_button.date_feel, state=Feel.wait2)

    dp.register_message_handler(status_button.name_status, state=Status.wait_st1)
    dp.register_message_handler(status_button.date_status, state=Status.wait_st2)


if __name__ == '__main__':
    action_btn = ActionButton(dp)
    action_btn.init_action_button()

    feel_btn = FeelButton(dp)
    feel_btn.init_feel_button()

    status_btn = StatusButton(dp)
    status_btn.init_status_button()

    register_handlers_food(dp)
    executor.start_polling(dp)
