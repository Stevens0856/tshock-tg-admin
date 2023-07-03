import logging

from aiogram import Router
from aiogram.filters import StateFilter, Text, or_f
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message

from filters.auth import IsAuth
from keyboards.keyboards import main_menu_kb, server_section_menu_kb, cancel_kb
from lexicon.default.message_texts import MAIN_MENU_TEXT, ERROR, NOT_AUTHORIZED_403
from lexicon.server_section.message_texts import WAITING_BROADCAST_INPUT, SERVER_SECTION_MENU_TEXT, \
    WAITING_RAW_CMD_INPUT, BROADCAST_200
from models.models import User
from services.api_requests import v2_server_status, world_read, v3_server_rawcmd, v2_server_broadcast
from services.services import convert_server_status_response_to_message, convert_world_read_response_to_message, \
    convert_raw_cmd_response_to_message
from states.states import FSMServerSection

router: Router = Router()
router.message.filter(StateFilter(FSMServerSection), IsAuth())
router.callback_query.filter(StateFilter(FSMServerSection), IsAuth())

log: logging.Logger = logging.getLogger('server_section')


@router.callback_query(StateFilter(FSMServerSection.menu), Text(text='back'))
async def process_back_to_main_menu(callback: CallbackQuery, state: FSMContext, language: str):
    await callback.message.delete()
    await callback.message.answer(text=MAIN_MENU_TEXT[language], reply_markup=main_menu_kb(language))
    await state.clear()


@router.callback_query(StateFilter(FSMServerSection.menu), Text(text='server_status'))
async def process_server_status(callback: CallbackQuery, language: str, user_data: User):
    server_status_result = await v2_server_status(user_data.api_token)
    await callback.message.delete()
    if server_status_result['status'] == '200':
        await callback.message.answer(text=convert_server_status_response_to_message(server_status_result, language),
                                      reply_markup=server_section_menu_kb(language))
    else:
        await callback.message.answer(text=ERROR[language],
                                      reply_markup=server_section_menu_kb(language))


@router.callback_query(StateFilter(FSMServerSection.menu), Text(text='world_read'))
async def process_world_read(callback: CallbackQuery, language: str, user_data: User):
    world_read_result = await world_read(user_data.api_token)
    await callback.message.delete()
    if world_read_result['status'] == '200':
        await callback.message.answer(text=convert_world_read_response_to_message(world_read_result, language),
                                      reply_markup=server_section_menu_kb(language))
    else:
        await callback.message.answer(text=ERROR[language],
                                      reply_markup=server_section_menu_kb(language))


@router.callback_query(StateFilter(FSMServerSection.menu), Text(text='broadcast'))
async def process_broadcast_start(callback: CallbackQuery, state: FSMContext, language: str):
    await callback.message.delete()
    await callback.message.answer(text=WAITING_BROADCAST_INPUT[language], reply_markup=cancel_kb(language))

    await state.set_state(FSMServerSection.broadcast)


@router.message(StateFilter(FSMServerSection.broadcast))
async def process_broadcast_input(message: Message, state: FSMContext, language: str, user_data: User):
    broadcast_result = await v2_server_broadcast(user_data.api_token, message.text)

    if broadcast_result['status'] == '200':
        await message.answer(text=BROADCAST_200[language],
                             reply_markup=server_section_menu_kb(language))
    elif broadcast_result['status'] == '403':
        await message.answer(text=NOT_AUTHORIZED_403[language],
                             reply_markup=server_section_menu_kb(language))
    else:
        await message.answer(text=ERROR[language], reply_markup=server_section_menu_kb(language))

    await state.set_state(FSMServerSection.menu)


@router.callback_query(StateFilter(FSMServerSection.menu), Text(text='raw_cmd'))
async def process_raw_cmd_start(callback: CallbackQuery, state: FSMContext, language: str):
    await callback.message.delete()
    await callback.message.answer(text=WAITING_RAW_CMD_INPUT[language], reply_markup=cancel_kb(language))

    await state.set_state(FSMServerSection.raw_cmd)


@router.message(StateFilter(FSMServerSection.raw_cmd))
async def process_raw_cmd_input(message: Message, state: FSMContext, language: str, user_data: User):
    raw_cmd_result = await v3_server_rawcmd(user_data.api_token, message.text)

    if raw_cmd_result['status'] == '200':
        await message.answer(text=convert_raw_cmd_response_to_message(raw_cmd_result['response'], language),
                             reply_markup=server_section_menu_kb(language))
    elif raw_cmd_result['status'] == '403':
        await message.answer(text=NOT_AUTHORIZED_403[language],
                             reply_markup=server_section_menu_kb(language))
    else:
        await message.answer(text=ERROR[language], reply_markup=server_section_menu_kb(language))

    await state.set_state(FSMServerSection.menu)


@router.callback_query(or_f(StateFilter(FSMServerSection.broadcast),
                            StateFilter(FSMServerSection.raw_cmd)),
                       Text(text='cancel'))
async def process_cancel_input(callback: CallbackQuery, state: FSMContext, language: str):
    await callback.message.delete()
    await callback.message.answer(text=SERVER_SECTION_MENU_TEXT[language],
                                  reply_markup=server_section_menu_kb(language))

    await state.set_state(FSMServerSection.menu)
