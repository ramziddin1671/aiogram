from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup



backvaksina = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🔙 Ortga", callback_data="cancelvaksina"),
        ],
    ])


backlocationvaksina = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🔙 Ortga", callback_data="cancelvaksina"),
        ],
        [
            InlineKeyboardButton(text="📍 Joylashuv", callback_data="locationVaksina"),
        ],
    ])