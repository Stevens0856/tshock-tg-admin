from aiogram import Router
from aiogram.filters import CommandStart, or_f, Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from filters.auth import IsAuth
from keyboards.keyboards import main_menu_kb
from lexicon.default.message_texts import MAIN_MENU_TEXT
from states.states import FSMAuthorization, FSMServerSection

router: Router = Router()
# Despite other filters, we explicitly prevent standard commands from running during input events
router.message.filter(~StateFilter(FSMAuthorization.input_api_token,
                                   FSMAuthorization.input_login,
                                   FSMAuthorization.input_password,
                                   FSMServerSection.broadcast))


@router.message(or_f(CommandStart(), Command(commands='menu')), IsAuth())
async def process_start_command(message: Message, state: FSMContext, language: str):
    await message.answer(text=MAIN_MENU_TEXT[language], reply_markup=main_menu_kb(language))
    await state.clear()


@router.message(Command(commands='setlanguage'), IsAuth())
async def process_start_command(message: Message):
    await message.answer(text='This is where the language change will start.')


@router.message(Command(commands='help'))
async def process_start_command(message: Message):
    await message.answer(text='Help with the bot.')
