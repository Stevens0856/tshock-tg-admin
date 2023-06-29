MAIN_MENU_TEXT: dict[str, str] = {
    'ru': '📜 Главное меню',
    'en': '📜 Main menu'
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
