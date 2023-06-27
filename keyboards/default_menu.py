from aiogram import Bot
from aiogram.types import BotCommand

from lexicon.default.menus import DEFAULT_MENU_COMMANDS


async def set_default_menu(bot: Bot):
    menu_commands = [BotCommand(
        command=command,
        description=description
    ) for command, description in DEFAULT_MENU_COMMANDS['en'].items()]
    await bot.set_my_commands(menu_commands)
