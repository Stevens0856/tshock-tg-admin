from aiogram import Router
from aiogram.filters import StateFilter, Text, Command, CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state
from aiogram.types import Message, CallbackQuery

from filters.auth import IsAuth
from states.states import FSMAuthorization
from lexicon.lexicon import WELCOME, LANG_SELECTED_IN_AUTH
from keyboards.keyboards import choose_language_kb, create_token_kb

router = Router()


# Fires on all messages if the user is not authorized. Moves to authorization state.
@router.message(~IsAuth(), StateFilter(default_state))
async def process_authorization_start(message: Message, state: FSMContext):
    await message.answer(text=WELCOME,
                         reply_markup=choose_language_kb())
    await state.set_state(FSMAuthorization.select_language)


@router.message(~IsAuth(), CommandStart())  # TODO: Попробовать объединить с фильтром выше, логика та же, фильтры разные
async def process_authorization_start(message: Message, state: FSMContext):
    await message.answer(text=WELCOME,
                         reply_markup=choose_language_kb())
    await state.set_state(FSMAuthorization.select_language)


# TODO: Написать хэндлер обрабатывающий некорректное сообщение в состоянии select_language


@router.callback_query(StateFilter(FSMAuthorization.select_language),
                       Text(text=['ru', 'en']))
async def process_choose_language(callback: CallbackQuery, state: FSMContext):
    await state.update_data(language=callback.data)
    await callback.message.delete()
    await callback.message.answer(text=LANG_SELECTED_IN_AUTH[callback.data],
                                  reply_markup=create_token_kb(callback.data))
    await state.set_state(FSMAuthorization.input_api_token)


@router.callback_query(StateFilter(FSMAuthorization.input_api_token),
                       Text(text=['back']))
async def process_choose_language(callback: CallbackQuery, state: FSMContext):
    await callback.message.delete()
    await callback.message.answer(text=WELCOME,
                                  reply_markup=choose_language_kb())
    await state.set_state(FSMAuthorization.select_language)


@router.message(Command(commands='cancel'), ~StateFilter(default_state))
async def process_cancel_command_state(message: Message, state: FSMContext):
    await message.answer(text='Выход из всех стадий')
    await state.clear()

