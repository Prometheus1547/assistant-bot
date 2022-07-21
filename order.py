from aiogram.dispatcher.filters.state import StatesGroup, State


class OrderFood(StatesGroup):
    waiting_for_food_name = State()
    # waiting_for_food_size = State()
    # waiting_for_food_loge = State()


class Feel(StatesGroup):
    wait1 = State()