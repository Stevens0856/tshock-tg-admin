import logging

from aiogram import Router
from aiogram.filters import StateFilter, Text
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery
from sqlalchemy.ext.asyncio import AsyncSession

from filters.auth import IsAuth
from keyboards.keyboards import main_menu_kb, confirmation_kb, tokens_section_menu_kb, choose_language_kb
from lexicon.auth.message_texts import WELCOME
from lexicon.default.message_texts import MAIN_MENU_TEXT
from lexicon.tokens_section.message_texts import LOGOUT_CONFIRMATION_TEXT, TOKENS_SECTION_MENU_TEXT, \
    SUCCESSFUL_LOGOUT_TEXT, GET_TOKEN_TEXT
from models.methods import delete_user
from models.models import User
from states.states import FSMTokensSection, FSMAuthorization

router: Router = Router()
router.message.filter(StateFilter(FSMTokensSection), IsAuth())
router.callback_query.filter(StateFilter(FSMTokensSection), IsAuth())

log: logging.Logger = logging.getLogger('tokens_section')


@router.callback_query(StateFilter(FSMTokensSection.menu), Text(text='back'))
async def process_back_to_main_menu(callback: CallbackQuery, state: FSMContext, language: str):
    await callback.message.delete()
    await callback.message.answer(text=MAIN_MENU_TEXT[language], reply_markup=main_menu_kb(language))
    await state.clear()


@router.callback_query(StateFilter(FSMTokensSection.menu), Text(text='logout'))
async def process_logout_start(callback: CallbackQuery, state: FSMContext, language: str):
    await callback.message.delete()
    await callback.message.answer(text=LOGOUT_CONFIRMATION_TEXT[language], reply_markup=confirmation_kb(language))

    await state.set_state(FSMTokensSection.logout)


@router.callback_query(StateFilter(FSMTokensSection.logout), Text(text='cancel'))
async def process_logout_cancel(callback: CallbackQuery, state: FSMContext, language: str):
    await callback.message.delete()
    await callback.message.answer(text=TOKENS_SECTION_MENU_TEXT[language],
                                  reply_markup=tokens_section_menu_kb(language))
    await state.set_state(FSMTokensSection.menu)


@router.callback_query(StateFilter(FSMTokensSection.logout), Text(text='confirm'))
async def process_logout_confirm(callback: CallbackQuery, state: FSMContext, language: str, session: AsyncSession):
    await callback.message.answer(text=SUCCESSFUL_LOGOUT_TEXT[language])
    await delete_user(session, callback.from_user.id)
    await callback.message.delete()
    await callback.message.answer(text=WELCOME, reply_markup=choose_language_kb())
    await state.clear()
    await state.set_state(FSMAuthorization.select_language)


@router.callback_query(StateFilter(FSMTokensSection.menu), Text(text='get_token'))
async def process_get_token(callback: CallbackQuery, language: str, user_data: User):
    user_token: str = user_data.api_token
    await callback.message.delete()
    await callback.message.answer(text=GET_TOKEN_TEXT[language]+'<span class="tg-spoiler">'+user_token+'</span>',
                                  reply_markup=tokens_section_menu_kb(language))
