import logging

from aiogram import Router
from aiogram.filters import StateFilter, Text, Command, CommandStart, or_f
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state
from aiogram.types import Message, CallbackQuery
from sqlalchemy.ext.asyncio import AsyncSession

from filters.auth import IsAuth
from models.methods import merge_user
from states.states import FSMAuthorization
from lexicon.lexicon import WELCOME, LANG_SELECTED_IN_AUTH, WARNING_CHOOSE_LANG, TOKEN_INPUT_200, TOKEN_INPUT_403, \
    ERROR, WAITING_TOKEN_INPUT, INPUT_LOGIN_TEXT, INPUT_PASSWORD_TEXT, TOKEN_CREATE_403, TOKEN_CREATE_200, \
    MAIN_MENU_TEXT
from keyboards.keyboards import choose_language_kb, create_token_kb, cancel_kb, main_menu_kb

from services.api_requests import tokentest, v2_token_create

router: Router = Router()

log: logging.Logger = logging.getLogger('authorization')


# Only fires if the user is not logged in. If it is not an authorization process or a /start command
@router.message(~IsAuth(), or_f(~StateFilter(FSMAuthorization), CommandStart()))
async def process_authorization_start(message: Message, state: FSMContext):
    await message.answer(text=WELCOME,
                         reply_markup=choose_language_kb())
    await state.set_state(FSMAuthorization.select_language)


# Handling language selection
@router.callback_query(StateFilter(FSMAuthorization.select_language),
                       Text(text=['ru', 'en']))
async def process_choose_language(callback: CallbackQuery, state: FSMContext):
    language: str = callback.data
    await state.update_data(language=language)
    await callback.message.delete()
    await callback.message.answer(text=LANG_SELECTED_IN_AUTH[language])
    await callback.message.answer(text=WAITING_TOKEN_INPUT[language],
                                  reply_markup=create_token_kb(language))
    await state.set_state(FSMAuthorization.input_api_token)


# Handling text messages when choosing a language
@router.message(StateFilter(FSMAuthorization.select_language))
async def warning_choose_language(message: Message):
    log.info(f"warning_choose_language | Message [TEXT: {message.text}] from user [ID: {message.from_user.id}]")
    await message.answer(text=WARNING_CHOOSE_LANG,
                         reply_markup=choose_language_kb())


# Handling the back button click
@router.callback_query(StateFilter(FSMAuthorization.input_api_token),
                       Text(text=['back']))
async def process_back_to_choose_language(callback: CallbackQuery, state: FSMContext):
    await callback.message.delete()
    await callback.message.answer(text=WELCOME,
                                  reply_markup=choose_language_kb())
    await state.set_state(FSMAuthorization.select_language)


# Handling token input
@router.message(StateFilter(FSMAuthorization.input_api_token))
async def process_token_input(message: Message, state: FSMContext, session: AsyncSession):
    log.info(f"process_token_input | Message [TEXT: {message.text}] from user [ID: {message.from_user.id}]")

    token_test_result: dict = await tokentest(message.text)
    state_data: dict = await state.get_data()
    if token_test_result['status'] == '403':
        await message.answer(text=TOKEN_INPUT_403[state_data['language']])
        await message.answer(text=WAITING_TOKEN_INPUT[state_data['language']],
                             reply_markup=create_token_kb(state_data['language']))
    elif token_test_result['status'] == '200':
        await message.answer(text=TOKEN_INPUT_200[state_data['language']])
        await message.answer(text=MAIN_MENU_TEXT[state_data['language']],
                             reply_markup=main_menu_kb(state_data['language']))
        await merge_user(session, message.from_user.id,
                         token_test_result['associateduser'], message.text, state_data['language'])
        await state.clear()
    else:
        await message.answer(text=ERROR[state_data['language']])
        await message.answer(text=WAITING_TOKEN_INPUT[state_data['language']],
                             reply_markup=create_token_kb(state_data['language']))


# Start creating a token
@router.callback_query(StateFilter(FSMAuthorization.input_api_token),
                       Text(text=['create_token']))
async def process_create_token_start(callback: CallbackQuery, state: FSMContext):
    state_data: dict = await state.get_data()

    await callback.message.delete()
    await callback.message.answer(text=INPUT_LOGIN_TEXT[state_data['language']],
                                  reply_markup=cancel_kb(state_data['language']))
    await state.set_state(FSMAuthorization.input_login)


# Handle pressing the cancel button when entering a login or password. Return to token input
@router.callback_query(or_f(StateFilter(FSMAuthorization.input_login), StateFilter(FSMAuthorization.input_password)),
                       Text(text=['cancel']))
async def process_create_token_start(callback: CallbackQuery, state: FSMContext):
    state_data: dict = await state.get_data()

    await callback.message.delete()
    await callback.message.answer(text=WAITING_TOKEN_INPUT[state_data['language']],
                                  reply_markup=create_token_kb(state_data['language']))

    await state.set_state(FSMAuthorization.input_api_token)


# Handling login input
@router.message(StateFilter(FSMAuthorization.input_login))
async def process_login_input(message: Message, state: FSMContext):
    log.info(f"process_login_input | Message [TEXT: {message.text}] from user [ID: {message.from_user.id}]")

    state_data: dict = await state.get_data()

    await state.update_data(login=message.text)
    await message.answer(text=INPUT_PASSWORD_TEXT[state_data['language']],
                         reply_markup=cancel_kb(state_data['language']))

    await state.set_state(FSMAuthorization.input_password)


# Handling password input. Creating a token and binding it
@router.message(StateFilter(FSMAuthorization.input_password))
async def process_password_input(message: Message, state: FSMContext, session: AsyncSession):
    log.info(f"process_password_input | Message [TEXT: {message.text}] from user [ID: {message.from_user.id}]")

    await state.update_data(password=message.text)
    state_data: dict = await state.get_data()

    token_create_result: dict = await v2_token_create(state_data['login'], state_data['password'])

    if token_create_result['status'] == '403':
        await message.answer(text=TOKEN_CREATE_403[state_data['language']])
        await message.answer(text=WAITING_TOKEN_INPUT[state_data['language']],
                             reply_markup=create_token_kb(state_data['language']))

        await state.set_state(FSMAuthorization.input_api_token)

    elif token_create_result['status'] == '200':
        await message.answer(text=TOKEN_CREATE_200[state_data['language']])
        await message.answer(text=MAIN_MENU_TEXT[state_data['language']],
                             reply_markup=main_menu_kb(state_data['language']))
        await merge_user(session, message.from_user.id,
                         state_data['login'], token_create_result['token'], state_data['language'])
        await state.clear()
    else:
        await message.answer(text=ERROR[state_data['language']])
        await message.answer(text=WAITING_TOKEN_INPUT[state_data['language']],
                             reply_markup=create_token_kb(state_data['language']))

        await state.set_state(FSMAuthorization.input_api_token)


@router.message(Command(commands='cancel'), ~StateFilter(default_state))
async def process_cancel_command_state(message: Message, state: FSMContext):
    await message.answer(text='Выход из всех стадий')
    await state.clear()
