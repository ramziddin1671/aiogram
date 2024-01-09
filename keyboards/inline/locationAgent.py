from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup



backagent = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🔙 Ortga", callback_data="cancelAgent"),
        ],
    ])

backagentxaqida = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🔙 Ortga", callback_data="cancelAgent"),
        ],
        [
            InlineKeyboardButton(text="📍 Joylashuv", callback_data="locationAgent"),
        ],
    ])