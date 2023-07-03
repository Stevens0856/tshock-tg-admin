import logging

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

from callback_factories.callback_factories import PaginationCallbackFactory, ActiveUsersCallbackFactory, \
    AllUsersCallbackFactory, AllUsersHeaderCallbackFactory
from lexicon.default.menus import BACK_BUTTON
from lexicon.default.message_texts import USER_ICON, PAGINATION_BUTTONS
from lexicon.users_section.menus import ALL_USERS_HEADER
from services.services import ActiveUsers, AllUsers

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


class UsersKeyboardCreator:
    def __init__(self, users: AllUsers | ActiveUsers, language: str, current_page: int = 1):
        self.users = users
        self.language = language
        self.current_page = current_page
        self.kb_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()

    def _add_pagination_and_back(self):
        pagination_buttons: list[InlineKeyboardButton] = [
            InlineKeyboardButton(text=PAGINATION_BUTTONS['backward'],
                                 callback_data=PaginationCallbackFactory(action='backward').pack()),
            InlineKeyboardButton(text=str(self.current_page) + '/' + str(self.users.page_count),
                                 callback_data=PaginationCallbackFactory(action='current_page').pack()),
            InlineKeyboardButton(text=PAGINATION_BUTTONS['forward'],
                                 callback_data=PaginationCallbackFactory(action='forward').pack())
        ]

        if self.users.page_count >= 5:
            pagination_buttons.insert(0, InlineKeyboardButton(text='1',
                                                              callback_data=PaginationCallbackFactory(
                                                                  action='start_page').pack()))
            pagination_buttons.append(InlineKeyboardButton(text=str(self.users.page_count),
                                                           callback_data=PaginationCallbackFactory(
                                                               action='last_page').pack()))

        self.kb_builder.row(*pagination_buttons)
        self.kb_builder.row(InlineKeyboardButton(text=BACK_BUTTON[self.language], callback_data='back'))

    def active_users(self):
        active_users_page_data: list = self.users.get_page_data(self.current_page)

        for user in active_users_page_data:
            self.kb_builder.row(InlineKeyboardButton(
                text=USER_ICON + ' ' + user,
                callback_data=ActiveUsersCallbackFactory(username=user).pack()))

        self._add_pagination_and_back()

        return self.kb_builder.as_markup()

    def all_users(self):
        header_buttons: list[InlineKeyboardButton] = [
            InlineKeyboardButton(text=ALL_USERS_HEADER[self.language]['id'],
                                 callback_data=AllUsersHeaderCallbackFactory(header='id').pack()),
            InlineKeyboardButton(text=ALL_USERS_HEADER[self.language]['username'],
                                 callback_data=AllUsersHeaderCallbackFactory(header='username').pack()),
            InlineKeyboardButton(text=ALL_USERS_HEADER[self.language]['group'],
                                 callback_data=AllUsersHeaderCallbackFactory(header='group').pack())
        ]

        self.kb_builder.row(*header_buttons)

        all_users_page_data: list = self.users.get_page_data(self.current_page)

        for user in all_users_page_data:
            users_buttons_row: list[InlineKeyboardButton] = [
                InlineKeyboardButton(text=user['id'],
                                     callback_data=AllUsersCallbackFactory(id=user['id'],
                                                                           username=user['name'],
                                                                           group=user['group']).pack()),
                InlineKeyboardButton(text=user['name'],
                                     callback_data=AllUsersCallbackFactory(id=user['id'],
                                                                           username=user['name'],
                                                                           group=user['group']).pack()),
                InlineKeyboardButton(text=user['group'],
                                     callback_data=AllUsersCallbackFactory(id=user['id'],
                                                                           username=user['name'],
                                                                           group=user['group']).pack())
            ]
            self.kb_builder.row(*users_buttons_row)

        self._add_pagination_and_back()

        return self.kb_builder.as_markup()
