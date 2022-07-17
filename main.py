import telebot
from telebot import types
from telebot.types import Message

import assistant_calls as requests
from configs import TOKEN_BOT

bot = telebot.TeleBot(TOKEN_BOT)


@bot.message_handler(commands=['start'])
def start(message: Message):
    markup = create_markup()
    bot.send_message(message.chat.id, 'Please choose something:', reply_markup=markup)


def create_markup():
    markup = types.InlineKeyboardMarkup()
    btn_action = types.InlineKeyboardButton(text='Action', callback_data='btn_action')
    btn_feel = types.InlineKeyboardButton(text='Feel', callback_data='btn_feel')
    btn_status = types.InlineKeyboardButton(text='Status', callback_data='btn_status')
    btn_event = types.InlineKeyboardButton(text='Event', callback_data='btn_event')
    markup.row(btn_action, btn_feel)
    markup.row(btn_status, btn_event)
    return markup


@bot.callback_query_handler(lambda c: c.data == 'btn_action')
def button_action_query(call: types.CallbackQuery):
    bot.answer_callback_query(call.id)
    chat_id = call.message.chat.id
    msg = bot.send_message(chat_id, 'Please enter the name:')
    bot.register_next_step_handler(msg, create_new_action)


def create_new_action(message: Message):
    requests.action_add(message.text)
    bot.send_message(message.chat.id, 'Action added.')


if __name__ == '__main__':
    bot.infinity_polling()
