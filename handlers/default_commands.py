from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from filters.auth import IsAuth
from keyboards.keyboards import main_menu_kb
from lexicon.lexicon import MAIN_MENU_TEXT

router: Router = Router()


@router.message(CommandStart(), IsAuth())
async def process_start_command(message: Message, language: str):
    await message.answer(text=MAIN_MENU_TEXT[language], reply_markup=main_menu_kb(language))
