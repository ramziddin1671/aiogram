from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

glav = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Bosh saxifaga'),

        ],
    ],
    resize_keyboard=True
)


menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='FTRA'),
            KeyboardButton(text="FMXM DUK"),

        ],
        [

            KeyboardButton(text="Zarur amaliyotlar markazi DUK"),
            KeyboardButton(text="ToshVZITI"),

        ],
        [
            KeyboardButton(text="O'zKFITI"),
            KeyboardButton(text="Sharq tabobati ITI"),
        ]
    ],
    resize_keyboard=True
)