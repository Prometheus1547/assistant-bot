from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


ikb_menu = InlineKeyboardMarkup(row_width=2,
                                inline_keyboard=[
                                    [
                                     InlineKeyboardButton(text='💪 Action', callback_data='Action'),
                                     InlineKeyboardButton(text='❤️ Feel', callback_data='Feel')
                                    ],
                                    [
                                     InlineKeyboardButton(text='👑 Status', callback_data='Status'),
                                     InlineKeyboardButton(text='🎉 Event', callback_data='Event'),
                                    ]
                                ])