from aiogram import Dispatcher

import commands.start
from states import States
from buttons import action_button, feel_button, status_button
from buttons.action_button import ActionButton
from buttons.feel_button import FeelButton
from buttons.status_button import StatusButton


def register_buttons(dp: Dispatcher):
    action_btn = ActionButton(dp)
    action_btn.init_action_button()

    feel_btn = FeelButton(dp)
    feel_btn.init_feel_button()

    status_btn = StatusButton(dp)
    status_btn.init_status_button()


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(commands.start.start, commands="start", state="*")

    dp.register_message_handler(action_button.name_action, state=States.wait_for_action_name)

    dp.register_message_handler(feel_button.name_feel, state=States.wait_for_feel_name)
    dp.register_message_handler(feel_button.estimation_feel, state=States.wait_for_feel_estimation)

    dp.register_message_handler(status_button.name_status, state=States.wait_for_status_name)
    dp.register_message_handler(status_button.date_status, state=States.wait_for_status_estimation)
