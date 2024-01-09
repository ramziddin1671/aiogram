from aiogram.dispatcher.filters.state import StatesGroup, State


class AdminStates(StatesGroup):
    Post = State()


class AdminPost(StatesGroup):
    NewMessage = State()
    Phone = State()
    Confirm = State()
    Reply = State()


class NewPost(StatesGroup):
    NewMessage = State()
    Phone = State()
    Confirm = State()


class Newnew(StatesGroup):
    NewMessage = State()
    Phone = State()
    Confirm = State()


class kamKariev(StatesGroup):
    NewMessage = State()
    Phone = State()
    Confirm = State()


class kamadmin(StatesGroup):
    NewMessage = State()
    Phone = State()
    Confirm = State()


class kaminayatov(StatesGroup):
    NewMessage = State()
    Phone = State()
    Confirm = State()


class AgentAdmin(StatesGroup):
    NewMessage = State()
    Phone = State()
    Confirm = State()


class AbduraxmonovKam(StatesGroup):
    NewMessage = State()
    Phone = State()
    Confirm = State()


class AzizovKam(StatesGroup):
    NewMessage = State()
    Phone = State()
    Confirm = State()


class MusaevKam(StatesGroup):
    NewMessage = State()
    Phone = State()
    Confirm = State()


class XasanovKam(StatesGroup):
    NewMessage = State()
    Phone = State()
    Confirm = State()


class AchilovKam(StatesGroup):
    NewMessage = State()
    Phone = State()
    Confirm = State()


class BoltaboevaKam(StatesGroup):
    NewMessage = State()
    Phone = State()
    Confirm = State()


class SalievaKam(StatesGroup):
    NewMessage = State()
    Phone = State()
    Confirm = State()

# Agentlik boshlandi
class KarievAgent(StatesGroup):
    NewMessage = State()
    Phone = State()
    Confirm = State()


class AkbarovAgent(StatesGroup):
    NewMessage = State()
    Phone = State()
    Confirm = State()


class TemirovAgent(StatesGroup):
    NewMessage = State()
    Phone = State()
    Confirm = State()


class BegmatovaAgent(StatesGroup):
    NewMessage = State()
    Phone = State()
    Confirm = State()

# Vaksina institut

class AshurovVaksina(StatesGroup):
    NewMessage = State()
    Phone = State()
    Confirm = State()


class MamatqulovVaksina(StatesGroup):
    NewMessage = State()
    Phone = State()
    Confirm = State()


class MaxmudjonovaVaksina(StatesGroup):
    NewMessage = State()
    Phone = State()
    Confirm = State()


class DadajonovVaksina(StatesGroup):
    NewMessage = State()
    Phone = State()
    Confirm = State()


class AsadulaevVaksina(StatesGroup):
    NewMessage = State()
    Phone = State()
    Confirm = State()


class AdminGxp(StatesGroup):
    NewMessage = State()
    Phone = State()
    Confirm = State()