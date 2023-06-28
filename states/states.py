from aiogram.filters.state import State, StatesGroup


class FSMLanguageReselection(StatesGroup):
    select_language = State()


class FSMAuthorization(StatesGroup):
    select_language = State()
    input_api_token = State()
    input_login = State()
    input_password = State()


class FSMServerSection(StatesGroup):
    menu = State()
    broadcast = State()
    raw_cmd = State()


class FSMUsersSection(StatesGroup):
    menu = State()
    active_users = State()
    all_users = State()


class FSMTokensSection(StatesGroup):
    menu = State()
    logout = State()
