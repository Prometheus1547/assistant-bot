from aiogram import Dispatcher

import commands.main_commands
from buttons import status_button, event_button
from buttons.event_button import EventButton
from buttons.status_button import StatusButton
from states import States


def register_buttons(dp: Dispatcher):
    status_btn = StatusButton(dp)
    status_btn.register_callback()

    event_btn = EventButton(dp)
    event_btn.register_callback()


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(commands.main_commands.start, commands="start", state="*")

    dp.register_message_handler(status_button.name_status, state=States.wait_for_status_name)
    dp.register_message_handler(status_button.estimation_status, state=States.wait_for_status_estimation)

    dp.register_message_handler(event_button.name_event, state=States.wait_for_event_name)
