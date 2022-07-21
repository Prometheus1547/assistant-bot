from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


ikb_menu = InlineKeyboardMarkup(row_width=2,
                                inline_keyboard=[
                                    [
                                     InlineKeyboardButton(text='💪 Action', callback_data='action'),
                                     InlineKeyboardButton(text='❤️ Feel', callback_data='feel')
                                    ],
                                    [
                                     InlineKeyboardButton(text='👑 Status', callback_data='status'),
                                     InlineKeyboardButton(text='🎉 Event', callback_data='event'),
                                    ]
                                ])