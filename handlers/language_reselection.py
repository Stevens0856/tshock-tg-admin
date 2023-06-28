import logging

from aiogram import Router
from aiogram.filters import StateFilter, Text
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery
from sqlalchemy.ext.asyncio import AsyncSession

from keyboards.keyboards import main_menu_kb
from lexicon.default.message_texts import MAIN_MENU_TEXT, ERROR
from lexicon.language.message_texts import LANG_RESELECTED
from models.methods import update_lang
from states.states import FSMLanguageReselection

router: Router = Router()

log: logging.Logger = logging.getLogger('language_reselection')


@router.callback_query(StateFilter(FSMLanguageReselection.select_language),
                       Text(text=['ru', 'en']))
async def process_language_reselection(callback: CallbackQuery, state: FSMContext, session: AsyncSession):
    language: str = callback.data
    await callback.message.delete()
    await state.clear()
    try:
        await update_lang(session, callback.from_user.id, language)
    except ValueError as e:
        log.error(f"process_language_reselection | ERROR [MSG: {str(e)}] from user [ID: {callback.from_user.id}] | "
                  f"LANG SELECTED: [{language}]")
        await callback.message.answer(text=ERROR[language])
        return

    await callback.message.answer(text=LANG_RESELECTED[language])
    await callback.message.answer(text=MAIN_MENU_TEXT[language], reply_markup=main_menu_kb(language))
