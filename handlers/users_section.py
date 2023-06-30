import logging

from aiogram import Router
from aiogram.filters import StateFilter, Text, or_f
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery

from filters.auth import IsAuth
from keyboards.keyboard_utils import create_inline_kb, create_active_users_kb
from keyboards.keyboards import main_menu_kb, users_section_menu_kb
from lexicon.default.message_texts import MAIN_MENU_TEXT, NOT_AUTHORIZED_403, ERROR
from lexicon.users_section.message_texts import USERS_SECTION_MENU_TEXT, NO_ACTIVE_USERS, ACTIVE_USERS_OPENING_TEXT
from models.models import User
from services.api_requests import v2_users_activelist, v2_users_list
from services.services import parse_active_users
from states.states import FSMUsersSection

router: Router = Router()
router.message.filter(StateFilter(FSMUsersSection), IsAuth())
router.callback_query.filter(StateFilter(FSMUsersSection), IsAuth())

log: logging.Logger = logging.getLogger('users_section')


@router.callback_query(StateFilter(FSMUsersSection.menu), Text(text='back'))
async def process_back_to_main_menu(callback: CallbackQuery, state: FSMContext, language: str):
    await callback.message.delete()
    await callback.message.answer(text=MAIN_MENU_TEXT[language], reply_markup=main_menu_kb(language))
    await state.clear()


@router.callback_query(StateFilter(FSMUsersSection.menu), Text(text='active_users'))
async def process_active_users(callback: CallbackQuery, state: FSMContext, user_data: User, language: str):
    active_users_result = await v2_users_activelist(user_data.api_token)
    await callback.message.delete()

    if active_users_result['status'] == '200':
        if not active_users_result['activeusers']:
            await callback.message.answer(text=NO_ACTIVE_USERS[language],
                                          reply_markup=users_section_menu_kb(language))
        else:
            active_users: list = parse_active_users(active_users_result['activeusers'])
            await callback.message.answer(text=ACTIVE_USERS_OPENING_TEXT[language],
                                          reply_markup=create_active_users_kb(active_users, 1, language))
            await state.set_state(FSMUsersSection.active_users)
    elif active_users_result['status'] == '403':
        await callback.message.answer(text=NOT_AUTHORIZED_403[language],
                                      reply_markup=users_section_menu_kb(language))
    else:
        await callback.message.answer(text=ERROR[language], reply_markup=users_section_menu_kb(language))

    log.info(f"process_active_users | Message [TEXT: {active_users_result}] from user [ID: {callback.from_user.id}]")


@router.callback_query(StateFilter(FSMUsersSection.menu), Text(text='all_users'))
async def process_all_users(callback: CallbackQuery, state: FSMContext, user_data: User):
    all_users_result = await v2_users_list(user_data.api_token)
    log.info(f"process_all_users | Message [TEXT: {all_users_result}] from user [ID: {callback.from_user.id}]")
    await callback.message.delete()
    await callback.message.answer(text='List of all registered users...',
                                  reply_markup=create_inline_kb(1, {'back': '<< Back'}))

    await state.set_state(FSMUsersSection.all_users)


@router.callback_query(or_f(StateFilter(FSMUsersSection.active_users),
                            StateFilter(FSMUsersSection.all_users)),
                       Text(text='back'))
async def process_back_to_users_section_menu(callback: CallbackQuery, state: FSMContext, language: str):
    await callback.message.delete()
    await callback.message.answer(text=USERS_SECTION_MENU_TEXT[language],
                                  reply_markup=users_section_menu_kb(language))
    await state.set_state(FSMUsersSection.menu)
