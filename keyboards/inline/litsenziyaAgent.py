from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.inline.AgentKeyboard import back_buttonkamitet
from keyboards.inline.callback_data import litsenziya_callback

litsenziyaAgent = {
    "Dori vositalari va tibbiy buyumlarni tayyorlash faoliyati bilan shug‘ullanish uchun moddiy-texnik baza, asbob-uskunalar, texnik vositalar va xodimlarga bo‘lgan talablar": "agenttalab1",
    "Dori vositalarini ishlab chiqarish faoliyati bilan shug‘ullanish uchun moddiy-texnik baza, asbob-uskunalar, texnik vositalar va xodimlarga bo‘lgan talablar": "agenttalab2",
    "Dori vositalari va tibbiy buyumlarni ulgurji realizatsiya qilish faoliyati bilan shug‘ullanish uchun  moddiy-texnik baza, asbob-uskunalar, texnik vositalar va xodimlarga bo‘lgan talablar": "agenttalab3",
    "🔙 Ortga" : "agenttalab4",
}

litsenziyalashagent = InlineKeyboardMarkup(row_width=1)
for key, value in litsenziyaAgent.items():
    litsenziyalashagent.insert(InlineKeyboardButton(text=key, callback_data=litsenziya_callback.new(item_name=value)))
