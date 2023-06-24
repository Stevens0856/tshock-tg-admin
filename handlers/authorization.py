from aiogram import Router
from aiogram.filters import StateFilter, Text, Command, CommandStart, or_f
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state
from aiogram.types import Message, CallbackQuery

from filters.auth import IsAuth
from states.states import FSMAuthorization
from lexicon.lexicon import WELCOME, LANG_SELECTED_IN_AUTH, WARNING_CHOOSE_LANG
from keyboards.keyboards import choose_language_kb, create_token_kb

router = Router()
# TODO: Повесить на весь роутер ~IsAuth() фильтр


# Only fires if the user is not logged in. If it is not an authorization process or a /start command
@router.message(~IsAuth(), or_f(~StateFilter(FSMAuthorization), CommandStart()))
async def process_authorization_start(message: Message, state: FSMContext):
    await message.answer(text=WELCOME,
                         reply_markup=choose_language_kb())
    await state.set_state(FSMAuthorization.select_language)


@router.callback_query(StateFilter(FSMAuthorization.select_language),
                       Text(text=['ru', 'en']))
async def process_choose_language(callback: CallbackQuery, state: FSMContext):
    await state.update_data(language=callback.data)
    await callback.message.delete()
    await callback.message.answer(text=LANG_SELECTED_IN_AUTH[callback.data],
                                  reply_markup=create_token_kb(callback.data))
    await state.set_state(FSMAuthorization.input_api_token)


@router.message(StateFilter(FSMAuthorization.select_language))
async def warning_choose_language(message: Message):
    await message.answer(text=WARNING_CHOOSE_LANG,
                         reply_markup=choose_language_kb())


@router.callback_query(StateFilter(FSMAuthorization.input_api_token),
                       Text(text=['back']))
async def process_back_to_choose_language(callback: CallbackQuery, state: FSMContext):
    await callback.message.delete()
    await callback.message.answer(text=WELCOME,
                                  reply_markup=choose_language_kb())
    await state.set_state(FSMAuthorization.select_language)


@router.message(Command(commands='cancel'), ~StateFilter(default_state))
async def process_cancel_command_state(message: Message, state: FSMContext):
    await message.answer(text='Выход из всех стадий')
    await state.clear()

