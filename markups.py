from telebot import types

start_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
start_markup_btn1 = types.KeyboardButton('ВТБ')
start_markup_btn2 = types.KeyboardButton('Сбербанк')
start_markup_btn3 = types.KeyboardButton('Тинькофф')
start_markup.row(start_markup_btn1)
start_markup.row(start_markup_btn2)
start_markup.row(start_markup_btn3)

source_markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
source_markup_btn1 = types.KeyboardButton('Доллар')
source_markup_btn2 = types.KeyboardButton('Евро')
source_markup.row(source_markup_btn1, source_markup_btn2)
source_markup_btn3 = types.KeyboardButton('Назад')
source_markup.row(source_markup_btn3)
