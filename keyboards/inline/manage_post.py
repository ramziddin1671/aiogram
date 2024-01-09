from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData

post_callback = CallbackData("create_post", "action")
test_callback = CallbackData("create_post", "action")
kar_callback = CallbackData("create_post", "action")
admin_callback = CallbackData("create_post", "action")
farmnadzor_callback = CallbackData("create_post", "action")
innayatov_callback = CallbackData("create_post", "action")
agentadmin_callback = CallbackData("create_post", "action")
AzizovKam_callback = CallbackData("create_post", "action")
MusaevKam_callback = CallbackData("create_post", "action")
XasanovKam_callback = CallbackData("create_post", "action")
AchilovKam_callback = CallbackData("create_post", "action")
BoltaboevaKam_callback = CallbackData("create_post", "action")
SalievaKam_callback = CallbackData("create_post", "action")
AbduraxmonovKam_callback = CallbackData("create_post", "action")
Adminbot_callback = CallbackData("create_post", "action")

#Agentlik boshlandi
KarievAgent_callback = CallbackData("create_post", "action")
AkbarovAgent_callback = CallbackData("create_post", "action")
TemirovAgent_callback = CallbackData("create_post", "action")
BegmatovaAgent_callback = CallbackData("create_post", "action")

#Vaksina Institut
Ashurov_Vaksina_callback = CallbackData("create_post", "action")
Mamatqulov_Vaksina_callback = CallbackData("create_post", "action")
Maxmudjonova_Vaksina_callback = CallbackData("create_post", "action")
Dadajonov_Vaksina_callback = CallbackData("create_post", "action")
Asadulaev_Vaksina_callback = CallbackData("create_post", "action")


#Gxp
AdminGxp_callback = CallbackData("create_post", "action")

confirmation_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[[
        InlineKeyboardButton(text="✅", callback_data=post_callback.new(action="post")),
        InlineKeyboardButton(text="❌ ", callback_data=post_callback.new(action="cancel")),
    ]]
)

test_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[[
        InlineKeyboardButton(text="✅", callback_data=test_callback.new(action="chop")),
        InlineKeyboardButton(text="❌ ", callback_data=test_callback.new(action="qayt")),
    ]]
)


kar_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[[
        InlineKeyboardButton(text="✅", callback_data=kar_callback.new(action="postKariev")),
        InlineKeyboardButton(text="❌ ", callback_data=kar_callback.new(action="cancelKariev")),
    ]]
)

admin_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[[
        InlineKeyboardButton(text="✅", callback_data=kar_callback.new(action="postadmin")),
        InlineKeyboardButton(text="❌ ", callback_data=kar_callback.new(action="canceladmin")),
    ]]
)

innayatov_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[[
        InlineKeyboardButton(text="✅", callback_data=kar_callback.new(action="postinayatov")),
        InlineKeyboardButton(text="❌ ", callback_data=kar_callback.new(action="cancelinayatov")),
    ]]
)

AgentAdmin_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[[
        InlineKeyboardButton(text="✅", callback_data=agentadmin_callback.new(action="postAgent")),
        InlineKeyboardButton(text="❌ ", callback_data=agentadmin_callback.new(action="cancelAgentadmin")),
    ]]
)

AzizovKam_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[[
        InlineKeyboardButton(text="✅", callback_data=AzizovKam_callback.new(action="postAzizov")),
        InlineKeyboardButton(text="❌ ", callback_data=AzizovKam_callback.new(action="cancelAzizov")),
    ]]
)

MusaevKam_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[[
        InlineKeyboardButton(text="✅", callback_data=MusaevKam_callback.new(action="postMusaev")),
        InlineKeyboardButton(text="❌ ", callback_data=MusaevKam_callback.new(action="cancelMusaev")),
    ]]
)

XasanovKam_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[[
        InlineKeyboardButton(text="✅", callback_data=XasanovKam_callback.new(action="postXasanov")),
        InlineKeyboardButton(text="❌ ", callback_data=XasanovKam_callback.new(action="cancelXasanov")),
    ]]
)

AchilovKam_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[[
        InlineKeyboardButton(text="✅", callback_data=AchilovKam_callback.new(action="postAchilov")),
        InlineKeyboardButton(text="❌ ", callback_data=AchilovKam_callback.new(action="cancelAchilov")),
    ]]
)

BoltaboevaKam_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[[
        InlineKeyboardButton(text="✅", callback_data=BoltaboevaKam_callback.new(action="postBoltaboeva")),
        InlineKeyboardButton(text="❌ ", callback_data=BoltaboevaKam_callback.new(action="cancelBoltaboeva")),
    ]]
)

SalievaKam_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[[
        InlineKeyboardButton(text="✅", callback_data=SalievaKam_callback.new(action="postSalieva")),
        InlineKeyboardButton(text="❌ ", callback_data=SalievaKam_callback.new(action="cancelSalieva")),
    ]]
)

AbduraxmonovKam_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[[
        InlineKeyboardButton(text="✅", callback_data=AbduraxmonovKam_callback.new(action="postAbduraxmonov")),
        InlineKeyboardButton(text="❌ ", callback_data=AbduraxmonovKam_callback.new(action="cancelAbduraxmonov")),
    ]]
)

#Agentlik boshlandi
KarievAgent_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[[
        InlineKeyboardButton(text="✅", callback_data=KarievAgent_callback.new(action="postKarievAgent")),
        InlineKeyboardButton(text="❌ ", callback_data=KarievAgent_callback.new(action="cancelKarievAgent")),
    ]]
)

AkbarovAgent_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[[
        InlineKeyboardButton(text="✅", callback_data=AkbarovAgent_callback.new(action="postAkbarovAgent")),
        InlineKeyboardButton(text="❌ ", callback_data=AkbarovAgent_callback.new(action="cancelAkbarovAgent")),
    ]]
)

TemirovAgent_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[[
        InlineKeyboardButton(text="✅", callback_data=TemirovAgent_callback.new(action="postTemirovAgent")),
        InlineKeyboardButton(text="❌ ", callback_data=TemirovAgent_callback.new(action="cancelTemirovAgent")),
    ]]
)

BegmatovaAgent_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[[
        InlineKeyboardButton(text="✅", callback_data=BegmatovaAgent_callback.new(action="postBegmatovagent")),
        InlineKeyboardButton(text="❌ ", callback_data=BegmatovaAgent_callback.new(action="cancelBegmatovaAgent")),
    ]]
)

# Vaksina Institut

Ashurov_Vaksina_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[[
        InlineKeyboardButton(text="✅", callback_data=Ashurov_Vaksina_callback.new(action="postAshurov_vaksina")),
        InlineKeyboardButton(text="❌ ", callback_data=Ashurov_Vaksina_callback.new(action="cancelAshurov_vaksina")),
    ]]
)

Mamatqulov_Vaksina_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[[
        InlineKeyboardButton(text="✅", callback_data=Mamatqulov_Vaksina_callback.new(action="postMamatqulov_vaksina")),
        InlineKeyboardButton(text="❌ ", callback_data=Mamatqulov_Vaksina_callback.new(action="cancelMamatqulov_vaksina")),
    ]]
)


Maxmudjonova_Vaksina_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[[
        InlineKeyboardButton(text="✅", callback_data=Maxmudjonova_Vaksina_callback.new(action="postMaxmudjonova_vaksina")),
        InlineKeyboardButton(text="❌ ", callback_data=Maxmudjonova_Vaksina_callback.new(action="cancelMaxmudjonova_vaksina")),
    ]]
)


Dadajonov_Vaksina_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[[
        InlineKeyboardButton(text="✅", callback_data=Dadajonov_Vaksina_callback.new(action="postDadajonov_vaksina")),
        InlineKeyboardButton(text="❌ ", callback_data=Dadajonov_Vaksina_callback.new(action="cancelDadajonov_vaksina")),
    ]]
)


Asadulaev_Vaksina_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[[
        InlineKeyboardButton(text="✅", callback_data=Asadulaev_Vaksina_callback.new(action="postAsadulaev_vaksina")),
        InlineKeyboardButton(text="❌ ", callback_data=Asadulaev_Vaksina_callback.new(action="cancelAsadulaev_vaksina")),
    ]]
)


AdminGxp_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[[
        InlineKeyboardButton(text="✅", callback_data=Asadulaev_Vaksina_callback.new(action="postAdminGxp_keyboard")),
        InlineKeyboardButton(text="❌ ", callback_data=Asadulaev_Vaksina_callback.new(action="cancelAdminGxp_keyboard")),
    ]]
)


farmnadzor_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[[
        InlineKeyboardButton(text="✅", callback_data=Asadulaev_Vaksina_callback.new(action="postfarmnadzor_keyboard")),
        InlineKeyboardButton(text="❌ ", callback_data=Asadulaev_Vaksina_callback.new(action="cancelfarmnadzor_keyboard")),
    ]]
)


adminbot_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[[
        InlineKeyboardButton(text="✅", callback_data=Asadulaev_Vaksina_callback.new(action="postadminbot_keyboard")),
        InlineKeyboardButton(text="❌ ", callback_data=Asadulaev_Vaksina_callback.new(action="canceladminbot_keyboard")),
    ]]
)
