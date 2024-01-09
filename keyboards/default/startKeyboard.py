from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menuStart = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text='Contact', request_contact=True),
            KeyboardButton(text='Location', request_location=True),
        ],
    ],
    resize_keyboard=True
)

CancelAdminBtn = ReplyKeyboardMarkup(resize_keyboard=True)
CancelAdminBtn.insert(KeyboardButton(text='❌ Bekon qilish (admin)'))