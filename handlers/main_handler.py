from aiogram import Dispatcher

import commands.main_commands
from buttons import action_button, feel_button, status_button, event_button
from buttons.action_button import ActionButton
from buttons.event_button import EventButton
from buttons.feel_button import FeelButton
from buttons.status_button import StatusButton
from states import States


def register_buttons(dp: Dispatcher):
    action_btn = ActionButton(dp)
    action_btn.register_callback()

    feel_btn = FeelButton(dp)
    feel_btn.register_callback()

    status_btn = StatusButton(dp)
    status_btn.register_callback()

    event_btn = EventButton(dp)
    event_btn.register_callback()


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(commands.main_commands.start, commands="start", state="*")

    dp.register_message_handler(action_button.name_action, state=States.wait_for_action_name)

    dp.register_message_handler(feel_button.name_feel, state=States.wait_for_feel_name)
    dp.register_message_handler(feel_button.estimation_feel, state=States.wait_for_feel_estimation)

    dp.register_message_handler(status_button.name_status, state=States.wait_for_status_name)
    dp.register_message_handler(status_button.estimation_status, state=States.wait_for_status_estimation)

    dp.register_message_handler(event_button.name_event, state=States.wait_for_event_name)
