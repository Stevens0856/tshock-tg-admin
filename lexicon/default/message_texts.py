MAIN_MENU_TEXT: dict[str, str] = {
    'ru': '<b>📟 Главное меню</b>',
    'en': '<b>📟 Main menu</b>'
}

HELP_TEXT: dict[str, str] = {
    'ru': '/menu - вызов основного меню\n'
          '/setlanguage - смена языка\n\n'
          'Созданный в боте токен является сессионным - при перезапуске Terraria-сервера он будет удален.\n'
          'Для доступа к некоторым разделам API необходимы соответствующие права.\n\n'
          'Связаться с разработчиком - @montaque',
    'en': '/menu - call the main menu\n'
          '/setlanguage - change language\n\n'
          'The token created in the bot is session token - it will be deleted when the Terraria server is restarted.\n'
          'Permissions are required to access certain parts of the API.\n\n'
          'Contact developer - @montaque'
}

ERROR: dict[str, str] = {
    'ru': '❗️Ошибка.\n'
          'Попробуйте позже.',
    'en': '❗️Error.\n'
          'Try later.'
}

TIME: dict[str, dict[str, str]] = {
    'ru': {
        'd': 'д',
        'h': 'ч',
        'm': 'м',
        's': 'с'
    },
    'en': {
        'd': 'd',
        'h': 'h',
        'm': 'm',
        's': 's'
    }
}

ACTIVITY_STATUS: dict[str, dict[bool, str]] = {
    'ru': {
        True: 'действует',
        False: 'отсутствует'
    },
    'en': {
        True: 'is active',
        False: 'is missing'
    }
}

NOT_AUTHORIZED_403: dict[str, str] = {
    'ru': '⛔️ У этой учетной записи нет прав для использования указанной конечной точки API.',
    'en': '⛔️ This account does not have permission to use the specified API endpoint.'
}

USER_ICON: str = '👤'

PAGINATION_BUTTONS: dict[str, str] = {
    'backward': '<<',
    'forward': '>>'
}
