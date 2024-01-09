from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton



Farm_nadzor = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Shifokor", callback_data="Shifokor_nadzor"),
            InlineKeyboardButton(text="Bemor", callback_data="Bemor_nadzor"),
        ],
        [
            InlineKeyboardButton(text="🔙 Ortga", callback_data="backnadzor"),
        ],
    ])