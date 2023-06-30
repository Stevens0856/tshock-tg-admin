DEFAULT_MENU_COMMANDS: dict[str, dict[str, str]] = {
    'en': {
        '/menu': 'Main menu',
        '/setlanguage': 'Switch language',
        '/help': 'Bot Help',
    }
}

CANCEL_MENU: dict[str, dict[str, str]] = {
    'ru': {
        'cancel': '❌ Отмена'
    },
    'en': {
        'cancel': '❌ Cancel'
    }
}

MAIN_MENU: dict[str, dict[str, str]] = {
    'ru': {
        'server': '⚙️ Сервер',
        'users': '👨‍🦰 Пользователи',
        'tokens': '🗝 Токены',
    },
    'en': {
        'server': '⚙️ Server',
        'users': '👨‍🦰 Users',
        'tokens': '🗝 Tokens',
    }
}

CONFIRMATION_MENU: dict[str, dict[str, str]] = {
    'ru': {
        'confirm': '✅ Подтвердить',
        'cancel': '❌ Отмена'
    },
    'en': {
        'confirm': '✅ Confirm',
        'cancel': '❌ Cancel'
    }
}

BACK_BUTTON: dict[str, str] = {
    'ru': '<< Назад',
    'en': '<< Back'
}
