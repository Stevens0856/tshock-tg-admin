import logging

from aiogram import Router
from aiogram.filters import StateFilter, Text
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message

from filters.auth import IsAuth
from keyboards.keyboards import main_menu_kb, server_section_menu_kb, cancel_kb
from lexicon.default.message_texts import MAIN_MENU_TEXT
from lexicon.server_section.message_texts import WAITING_BROADCAST_INPUT, SERVER_SECTION_MENU_TEXT, \
    WAITING_RAW_CMD_INPUT
from states.states import FSMServerSection

router: Router = Router()
router.message.filter(IsAuth(), StateFilter(FSMServerSection))
router.callback_query.filter(IsAuth(), StateFilter(FSMServerSection))

log: logging.Logger = logging.getLogger('server_section')


@router.callback_query(StateFilter(FSMServerSection.menu), Text(text='back'))
async def process_back_to_main_menu(callback: CallbackQuery, state: FSMContext, language: str):
    await callback.message.delete()
    await callback.message.answer(text=MAIN_MENU_TEXT[language], reply_markup=main_menu_kb(language))
    await state.clear()


@router.callback_query(StateFilter(FSMServerSection.menu), Text(text='server_status'))
async def process_server_status(callback: CallbackQuery, language: str):
    await callback.message.delete()
    await callback.message.answer(text='Server status info...', reply_markup=server_section_menu_kb(language))


@router.callback_query(StateFilter(FSMServerSection.menu), Text(text='world_read'))
async def process_world_read(callback: CallbackQuery, language: str):
    await callback.message.delete()
    await callback.message.answer(text='World Information...', reply_markup=server_section_menu_kb(language))


@router.callback_query(StateFilter(FSMServerSection.menu), Text(text='broadcast'))
async def process_broadcast_start(callback: CallbackQuery, state: FSMContext, language: str):
    await callback.message.delete()
    await callback.message.answer(text=WAITING_BROADCAST_INPUT[language], reply_markup=cancel_kb(language))

    await state.set_state(FSMServerSection.broadcast)


@router.message(StateFilter(FSMServerSection.broadcast))
async def process_broadcast_input(message: Message, state: FSMContext, language: str):
    await message.answer(text='Message sent to server...',
                         reply_markup=server_section_menu_kb(language))

    await state.set_state(FSMServerSection.menu)


@router.callback_query(StateFilter(FSMServerSection.broadcast), Text(text='cancel'))
async def process_cancel_broadcast(callback: CallbackQuery, state: FSMContext, language: str):
    await callback.message.delete()
    await callback.message.answer(text=SERVER_SECTION_MENU_TEXT[language],
                                  reply_markup=server_section_menu_kb(language))

    await state.set_state(FSMServerSection.menu)


@router.callback_query(StateFilter(FSMServerSection.menu), Text(text='raw_cmd'))
async def process_raw_cmd_start(callback: CallbackQuery, state: FSMContext, language: str):
    await callback.message.delete()
    await callback.message.answer(text=WAITING_RAW_CMD_INPUT[language], reply_markup=cancel_kb(language))

    await state.set_state(FSMServerSection.raw_cmd)


@router.message(StateFilter(FSMServerSection.raw_cmd))
async def process_raw_cmd_input(message: Message, state: FSMContext, language: str):
    await message.answer(text='Command completed...',
                         reply_markup=server_section_menu_kb(language))

    await state.set_state(FSMServerSection.menu)


@router.callback_query(StateFilter(FSMServerSection.raw_cmd), Text(text='cancel'))
async def process_cancel_raw_cmd(callback: CallbackQuery, state: FSMContext, language: str):
    await callback.message.delete()
    await callback.message.answer(text=SERVER_SECTION_MENU_TEXT[language],
                                  reply_markup=server_section_menu_kb(language))

    await state.set_state(FSMServerSection.menu)
