import logging

from aiogram import Router
from aiogram.filters import StateFilter, Text, or_f
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery

from callback_factories.callback_factories import PaginationCallbackFactory, ActiveUsersCallbackFactory, \
    AllUsersCallbackFactory, AllUsersHeaderCallbackFactory
from filters.auth import IsAuth
from keyboards.keyboard_utils import UsersKeyboardCreator
from keyboards.keyboards import main_menu_kb, users_section_menu_kb
from lexicon.default.message_texts import MAIN_MENU_TEXT, NOT_AUTHORIZED_403, ERROR
from lexicon.users_section.message_texts import USERS_SECTION_MENU_TEXT, NO_ACTIVE_USERS, ACTIVE_USERS_OPENING_TEXT, \
    ALL_USERS_OPENING_TEXT, NO_REGISTERED_USERS
from models.models import User
from services.api_requests import v2_users_activelist, v2_users_list
from services.services import ActiveUsers, AllUsers
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
        if active_users_result['activeusers']:
            active_users: ActiveUsers = ActiveUsers(active_users_result['activeusers'])
            keyboard_creator: UsersKeyboardCreator = UsersKeyboardCreator(active_users, language)
            await callback.message.answer(text=ACTIVE_USERS_OPENING_TEXT[language],
                                          reply_markup=keyboard_creator.active_users())
            await state.update_data(current_page=1)
            await state.set_state(FSMUsersSection.active_users)
        else:
            await callback.message.answer(text=NO_ACTIVE_USERS[language],
                                          reply_markup=users_section_menu_kb(language))
    elif active_users_result['status'] == '403':
        await callback.message.answer(text=NOT_AUTHORIZED_403[language],
                                      reply_markup=users_section_menu_kb(language))
    else:
        await callback.message.answer(text=ERROR[language], reply_markup=users_section_menu_kb(language))


@router.callback_query(StateFilter(FSMUsersSection.active_users), PaginationCallbackFactory.filter())
async def process_active_users_page_switching(callback: CallbackQuery, callback_data: PaginationCallbackFactory,
                                              state: FSMContext, user_data: User, language: str):
    active_users_result = await v2_users_activelist(user_data.api_token)
    await callback.message.delete()
    if active_users_result['status'] == '200':
        if active_users_result['activeusers']:
            active_users: ActiveUsers = ActiveUsers(active_users_result['activeusers'])
            current_page: int = (await state.get_data())['current_page']
            target_page: int = active_users.get_target_page(callback_data.action, current_page)
            keyboard_creator: UsersKeyboardCreator = UsersKeyboardCreator(active_users,
                                                                          language,
                                                                          target_page)
            await callback.message.answer(text=ACTIVE_USERS_OPENING_TEXT[language],
                                          reply_markup=keyboard_creator.active_users())
            await state.update_data(current_page=target_page)
            return
        else:
            await callback.message.answer(text=NO_ACTIVE_USERS[language],
                                          reply_markup=users_section_menu_kb(language))
    elif active_users_result['status'] == '403':
        await callback.message.answer(text=NOT_AUTHORIZED_403[language],
                                      reply_markup=users_section_menu_kb(language))
    else:
        await callback.message.answer(text=ERROR[language], reply_markup=users_section_menu_kb(language))

    await state.set_state(FSMUsersSection.menu)


@router.callback_query(StateFilter(FSMUsersSection.active_users), ActiveUsersCallbackFactory.filter())
async def process_active_user_click(callback: CallbackQuery):
    await callback.answer()


@router.callback_query(StateFilter(FSMUsersSection.menu), Text(text='all_users'))
async def process_all_users(callback: CallbackQuery, state: FSMContext, user_data: User, language: str):
    all_users_result = await v2_users_list(user_data.api_token)
    await callback.message.delete()
    if all_users_result['status'] == '200':
        if all_users_result['users']:
            all_users: AllUsers = AllUsers(all_users_result['users'])
            keyboard_creator: UsersKeyboardCreator = UsersKeyboardCreator(all_users, language)
            await callback.message.answer(text=ALL_USERS_OPENING_TEXT[language],
                                          reply_markup=keyboard_creator.all_users())
            await state.update_data(current_page=1)
            await state.set_state(FSMUsersSection.all_users)
        else:
            await callback.message.answer(text=NO_REGISTERED_USERS[language],
                                          reply_markup=users_section_menu_kb(language))
    elif all_users_result['status'] == '403':
        await callback.message.answer(text=NOT_AUTHORIZED_403[language],
                                      reply_markup=users_section_menu_kb(language))
    else:
        await callback.message.answer(text=ERROR[language], reply_markup=users_section_menu_kb(language))


@router.callback_query(StateFilter(FSMUsersSection.all_users), PaginationCallbackFactory.filter())
async def process_all_users_page_switching(callback: CallbackQuery, callback_data: PaginationCallbackFactory,
                                           state: FSMContext, user_data: User, language: str):
    all_users_result = await v2_users_list(user_data.api_token)
    await callback.message.delete()
    if all_users_result['status'] == '200':
        if all_users_result['users']:
            all_users: AllUsers = AllUsers(all_users_result['users'])
            current_page: int = (await state.get_data())['current_page']
            target_page: int = all_users.get_target_page(callback_data.action, current_page)
            keyboard_creator: UsersKeyboardCreator = UsersKeyboardCreator(all_users,
                                                                          language,
                                                                          target_page)
            await callback.message.answer(text=ALL_USERS_OPENING_TEXT[language],
                                          reply_markup=keyboard_creator.all_users())
            await state.update_data(current_page=target_page)
            return
        else:
            await callback.message.answer(text=NO_REGISTERED_USERS[language],
                                          reply_markup=users_section_menu_kb(language))
    elif all_users_result['status'] == '403':
        await callback.message.answer(text=NOT_AUTHORIZED_403[language],
                                      reply_markup=users_section_menu_kb(language))
    else:
        await callback.message.answer(text=ERROR[language], reply_markup=users_section_menu_kb(language))

    await state.set_state(FSMUsersSection.menu)


@router.callback_query(StateFilter(FSMUsersSection.all_users), AllUsersCallbackFactory.filter())
async def process_registered_user_click(callback: CallbackQuery):
    await callback.answer()


@router.callback_query(StateFilter(FSMUsersSection.all_users), AllUsersHeaderCallbackFactory.filter())
async def process_all_users_header_click(callback: CallbackQuery):
    await callback.answer()


@router.callback_query(or_f(StateFilter(FSMUsersSection.active_users),
                            StateFilter(FSMUsersSection.all_users)),
                       Text(text='back'))
async def process_back_to_users_section_menu(callback: CallbackQuery, state: FSMContext, language: str):
    await callback.message.delete()
    await callback.message.answer(text=USERS_SECTION_MENU_TEXT[language],
                                  reply_markup=users_section_menu_kb(language))
    await state.set_state(FSMUsersSection.menu)
