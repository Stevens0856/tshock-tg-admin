import logging

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

from callback_factories.callback_factories import PaginationCallbackFactory
from lexicon.default.menus import BACK_BUTTON
from lexicon.default.message_texts import USER_ICON, PAGINATION_BUTTONS
from services.services import ActiveUsers

log: logging.Logger = logging.getLogger('keyboard_utils')


def create_inline_kb(width: int,
                     button_dict: dict | None = None,
                     last_btn: str | None = None,
                     last_btn_data: str | None = None) -> InlineKeyboardMarkup:
    kb_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
    buttons: list[InlineKeyboardButton] = []

    if button_dict:
        for button, text in button_dict.items():
            buttons.append(InlineKeyboardButton(
                text=text,
                callback_data=button))

    kb_builder.row(*buttons, width=width)
    if last_btn:
        kb_builder.row(InlineKeyboardButton(
            text=last_btn,
            callback_data=last_btn_data if last_btn_data else 'cancel'))

    return kb_builder.as_markup()


def create_active_users_kb(active_users: ActiveUsers, language: str, current_page: int = 1) -> InlineKeyboardMarkup:
    kb_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
    buttons_with_users: list[InlineKeyboardButton] = []

    active_users_page_data: list = active_users.get_page_data(current_page)

    for user in active_users_page_data:
        buttons_with_users.append(InlineKeyboardButton(
            text=USER_ICON + ' ' + user,
            callback_data=user))

    kb_builder.row(*buttons_with_users, width=1)

    pagination_buttons: list[InlineKeyboardButton] = [
        InlineKeyboardButton(text=PAGINATION_BUTTONS['backward'],
                             callback_data=PaginationCallbackFactory(action='backward').pack()),
        InlineKeyboardButton(text=str(current_page) + '/' + str(active_users.page_count),
                             callback_data=PaginationCallbackFactory(action='current_page').pack()),
        InlineKeyboardButton(text=PAGINATION_BUTTONS['forward'],
                             callback_data=PaginationCallbackFactory(action='forward').pack())
    ]

    if active_users.page_count >= 5:
        pagination_buttons.insert(0, InlineKeyboardButton(text='1',
                                                          callback_data=PaginationCallbackFactory(
                                                             action='start_page').pack()))
        pagination_buttons.append(InlineKeyboardButton(text=str(active_users.page_count),
                                                       callback_data=PaginationCallbackFactory(
                                                           action='last_page').pack()))

    kb_builder.row(*pagination_buttons)
    kb_builder.row(InlineKeyboardButton(text=BACK_BUTTON[language], callback_data='back'))

    return kb_builder.as_markup()
