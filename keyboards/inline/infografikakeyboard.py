from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.inline.AgentKeyboard import back_buttonkamitet, back_button
from keyboards.inline.callback_data import bolinmacamitet_callback, infografik_callback

infoagent = {
    "Dorixonalarda bo‘lishi majburiy bo‘lgan tibbiy buyumlar nimalardan iborat?": "agentdorimajburiy",
    "Dorixonada dori vositasi uchun tovar cheki berish majburiymi?": "agentchek",
    "Litsenziyalash va nazorat qilish boshqarmasining 2…": "agentnazorat",
    "Litsenziyalash va nazorat qilish boshqarmasining farmatsevtika faoliyatini...": "agentboshqarma",
    "Ulgurji realizatsiya qiluvchi tashkilotlar dori vositalari va tibbiy buyumlarni...": "agentulgurji",
    "Dori vositalari va tibbiy buyumlarni chakana realizatsiya qilish bundan m…": "agenytchakana",
    "GxP - bu farmatsevtika sohasida qo‘llaniladigan va barcha ilg‘or usullar…": "agentgp",
    "Qo‘llash uchun yaroqsiz dori vositalari va tibbiy buyumlar ularning egalarining yoki sudning qarori…": "agentyaroqsiz",

}

infograficagent = InlineKeyboardMarkup(row_width=1)
for key, value in infoagent.items():
    infograficagent.insert(InlineKeyboardButton(text=key, callback_data=infografik_callback.new(item_name=value)))
infograficagent.insert(back_button)