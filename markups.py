from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton

inline_markup_main = InlineKeyboardMarkup(row_width=2,
                                          inline_keyboard=[
                                    [
                                        InlineKeyboardButton(text='Action', callback_data='action'),
                                        InlineKeyboardButton(text='Feel', callback_data='feel')
                                    ],
                                    [
                                        InlineKeyboardButton(text='Status', callback_data='status'),
                                        InlineKeyboardButton(text='Event', callback_data='event'),
                                    ]
                                ])

keyboard_for_feel = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True,
                                        keyboard=[
                                    [
                                        KeyboardButton(text='Energy'),
                                        KeyboardButton(text='Focus'),
                                    ],
[
                                        KeyboardButton(text='Health'),
                                        KeyboardButton(text='Mood'),
                                    ]



]



)