from aiogram.dispatcher.filters.state import StatesGroup, State


class States(StatesGroup):
    wait_for_action_name = State()

    wait_for_feel_name = State()
    wait_for_feel_estimation = State()

    wait_for_status_name = State()
    wait_for_status_estimation = State()

    wait_for_event_name = State()

