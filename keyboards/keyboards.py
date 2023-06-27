from keyboards.keyboard_utils import create_inline_kb
from lexicon.default.menus import LANGUAGE_MENU, CANCEL_MENU, MAIN_MENU
from lexicon.auth.menus import CREATE_SESSION_TOKEN_MENU


def choose_language_kb():
    return create_inline_kb(1, LANGUAGE_MENU)


def create_token_kb(lang):
    return create_inline_kb(1, CREATE_SESSION_TOKEN_MENU[lang])


def cancel_kb(lang):
    return create_inline_kb(1, CANCEL_MENU[lang])


def main_menu_kb(lang):
    return create_inline_kb(1, MAIN_MENU[lang])
