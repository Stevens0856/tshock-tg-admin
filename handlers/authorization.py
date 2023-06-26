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
    ERROR, WAITING_TOKEN_INPUT
from keyboards.keyboards import choose_language_kb, create_token_kb

from services.api_requests import tokentest

router = Router()
# TODO: Повесить на весь роутер ~IsAuth() фильтр

log = logging.getLogger('authorization')


# Only fires if the user is not logged in. If it is not an authorization process or a /start command
@router.message(~IsAuth(), or_f(~StateFilter(FSMAuthorization), CommandStart()))
async def process_authorization_start(message: Message, state: FSMContext):
    await message.answer(text=WELCOME,
                         reply_markup=choose_language_kb())
    await state.set_state(FSMAuthorization.select_language)


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


@router.message(StateFilter(FSMAuthorization.select_language))
async def warning_choose_language(message: Message):
    log.info(f"warning_choose_language | Message [TEXT: {message.text}] from user [ID: {message.from_user.id}]")
    await message.answer(text=WARNING_CHOOSE_LANG,
                         reply_markup=choose_language_kb())


@router.callback_query(StateFilter(FSMAuthorization.input_api_token),
                       Text(text=['back']))
async def process_back_to_choose_language(callback: CallbackQuery, state: FSMContext):
    await callback.message.delete()
    await callback.message.answer(text=WELCOME,
                                  reply_markup=choose_language_kb())
    await state.set_state(FSMAuthorization.select_language)


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
        await message.answer(text='Отображение меню.')
        await merge_user(session, message.from_user.id,
                         token_test_result['associateduser'], message.text, state_data['language'])
        await state.clear()
    else:
        await message.answer(text=ERROR[state_data['language']])
        await message.answer(text=WAITING_TOKEN_INPUT[state_data['language']],
                             reply_markup=create_token_kb(state_data['language']))


@router.message(Command(commands='cancel'), ~StateFilter(default_state))
async def process_cancel_command_state(message: Message, state: FSMContext):
    await message.answer(text='Выход из всех стадий')
    await state.clear()
