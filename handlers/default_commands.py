from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from filters.auth import IsAuth

router = Router()


@router.message(CommandStart(), IsAuth())
async def process_start_command(message: Message):
    await message.answer(text='Пользователь зарегистрирован.\n\n'
                              'Тут должно появляться главное меню.')


@router.message(CommandStart(), ~IsAuth())
async def process_start_command(message: Message):
    await message.answer(text='Пользователь не зарегистрирован.\n\n'
                              'Тут будет начинаться логика регистрации пользователя.')
