from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

import commands.start
from buttons import action_button, feel_button, status_button
from buttons.action_button import ActionButton
from buttons.feel_button import FeelButton
from buttons.status_button import StatusButton
from config import TOKEN
from order import Action, Feel, Status


def register_buttons(dp: Dispatcher):
    action_btn = ActionButton(dp)
    action_btn.init_action_button()

    feel_btn = FeelButton(dp)
    feel_btn.init_feel_button()

    status_btn = StatusButton(dp)
    status_btn.init_status_button()


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(commands.start.start, commands="start", state="*")
    dp.register_message_handler(action_button.name_action, state=Action.state_action)

    dp.register_message_handler(feel_button.name_feel, state=Feel.wait1)
    dp.register_message_handler(feel_button.date_feel, state=Feel.wait2)

    dp.register_message_handler(status_button.name_status, state=Status.wait_st1)
    dp.register_message_handler(status_button.date_status, state=Status.wait_st2)
