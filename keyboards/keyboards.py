from keyboards.keyboard_utils import create_inline_kb
from lexicon.lexicon import LANGUAGE_MENU, CREATE_SESSION_TOKEN_MENU


def choose_language_kb():
    return create_inline_kb(1, LANGUAGE_MENU)


def create_token_kb(lang):
    return create_inline_kb(1, CREATE_SESSION_TOKEN_MENU[lang])
