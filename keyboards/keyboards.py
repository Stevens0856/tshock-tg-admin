from keyboards.keyboard_utils import create_inline_kb
from lexicon.default.menus import LANGUAGE_MENU, CANCEL_MENU, MAIN_MENU, CONFIRMATION_MENU
from lexicon.auth.menus import CREATE_SESSION_TOKEN_MENU
from lexicon.server_section.menus import SERVER_SECTION_MENU
from lexicon.tokens_section.menus import TOKENS_SECTION_MENU
from lexicon.users_section.menus import USERS_SECTION_MENU


def choose_language_kb():
    return create_inline_kb(1, LANGUAGE_MENU)


def create_token_kb(lang):
    return create_inline_kb(1, CREATE_SESSION_TOKEN_MENU[lang])


def cancel_kb(lang):
    return create_inline_kb(1, CANCEL_MENU[lang])


def main_menu_kb(lang):
    return create_inline_kb(1, MAIN_MENU[lang])


def server_section_menu_kb(lang):
    return create_inline_kb(1, SERVER_SECTION_MENU[lang])


def users_section_menu_kb(lang):
    return create_inline_kb(1, USERS_SECTION_MENU[lang])


def tokens_section_menu_kb(lang):
    return create_inline_kb(1, TOKENS_SECTION_MENU[lang])


def confirmation_kb(lang):
    return create_inline_kb(2, CONFIRMATION_MENU[lang])
