from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder


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
