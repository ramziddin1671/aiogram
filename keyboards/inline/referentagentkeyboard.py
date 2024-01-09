from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

Referent = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="05.01.2023", callback_data="02_avgust"),
        ],
        [
            InlineKeyboardButton(text="🔙 Ortga", callback_data="cancelAgent"),
        ],
    ])