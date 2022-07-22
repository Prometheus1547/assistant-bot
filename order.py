from aiogram.dispatcher.filters.state import StatesGroup, State


class Action(StatesGroup):
    state_action = State()

class Feel(StatesGroup):
    wait1 = State()
    wait2 = State()

class Status(StatesGroup):
    wait_st1 = State()
    wait_st2 = State()