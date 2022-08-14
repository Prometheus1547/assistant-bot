from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton

inline_markup_main = InlineKeyboardMarkup(row_width=2,
                                          inline_keyboard=[
                                              [
                                                  InlineKeyboardButton(text='Status', callback_data='status'),
                                                  InlineKeyboardButton(text='Event', callback_data='event'),
                                              ]])

keyboard_for_status = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True,
                                          keyboard=[
                                              [
                                                  KeyboardButton(text='Energy'),
                                                  KeyboardButton(text='Focus'),
                                              ],
                                              [
                                                  KeyboardButton(text='Health'),
                                                  KeyboardButton(text='Mood'),
                                              ]])

keyboard_for_estimation = ReplyKeyboardMarkup(row_width=3, resize_keyboard=True,
                                              keyboard=[
                                                  [
                                                      KeyboardButton(text='0'),
                                                      KeyboardButton(text='20'),
                                                      KeyboardButton(text='40'),
                                                  ],
                                                  [
                                                      KeyboardButton(text='60'),
                                                      KeyboardButton(text='80'),
                                                      KeyboardButton(text='100'),
                                                  ]])
