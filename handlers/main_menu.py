import logging

from aiogram import Router
from aiogram.filters import StateFilter, Text
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state
from aiogram.types import CallbackQuery

from filters.auth import IsAuth
from keyboards.keyboards import server_section_menu_kb
from lexicon.server_section.message_texts import SERVER_SECTION_MENU_TEXT
from states.states import FSMServerSection

router: Router = Router()
router.callback_query.filter(IsAuth(), StateFilter(default_state))

log: logging.Logger = logging.getLogger('main_menu')


@router.callback_query(Text(text='server'))
async def process_server_section(callback: CallbackQuery, state: FSMContext, language: str):

    await callback.message.delete()
    await callback.message.answer(text=SERVER_SECTION_MENU_TEXT[language],
                                  reply_markup=server_section_menu_kb(language))
    await state.set_state(FSMServerSection.menu)
