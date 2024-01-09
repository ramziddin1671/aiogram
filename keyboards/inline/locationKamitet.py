from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup



backkamitet = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🔙 Ortga", callback_data="cancelKamitet"),
        ],
    ])


backkamitetxaqida = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🔙 Ortga", callback_data="cancelKamitet"),
        ],
        [
            InlineKeyboardButton(text="📍 Joylashuv", callback_data="locationKamitet"),
        ],
    ])

backGxp = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🔙 Ortga", callback_data="cancelGxp"),
        ],
        [
            InlineKeyboardButton(text="📍 Location", callback_data="locationGxp"),
        ],
    ])


backbackGxp = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🔙 Ortga", callback_data="cancelGxp"),
        ],
    ])

RAXBARGxp = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🔙 Ortga", callback_data="raxbarcancelGxp"),
        ],
    ])