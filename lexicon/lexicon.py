DEFAULT_MENU_COMMANDS: dict[str, dict[str, str]] = {
    'en': {
        '/menu': 'Main menu',
        '/setlanguage': 'Switch language',
        '/help': 'Bot Help',
    }
}

WELCOME: str = 'Добро пожаловать! / Welcome!\n''Выберите язык. / Choose language.'

LANGUAGE_MENU: dict[str, str] = {
    'ru': '🇷🇺 Русский',
    'en': '🏴󠁧󠁢󠁥󠁮󠁧󠁿 English',
}

LANG_SELECTED_IN_AUTH: dict[str, str] = {
    'ru': '🇷🇺 Выбран русский язык.\n'
          'Теперь необходимо привязать серверный токен.\n',
    'en': '🏴󠁧󠁢󠁥󠁮󠁧󠁿 English is selected.\n'
          'Now we need to bind the server token.\n'
}

WAITING_TOKEN_INPUT: dict[str, str] = {
    'ru': 'Пожалуйста, отправьте токен или создайте новый.',
    'en': 'Please submit a token or create a new one.'
}

WARNING_CHOOSE_LANG: str = 'Чтобы продолжить, необходимо выбрать язык. / To continue, you must select a language.'

TOKEN_INPUT_403: dict[str, str] = {
    'ru': '❗️Предоставленный токен недействителен.',
    'en': '❗️Provided token was not valid.'
}

TOKEN_INPUT_200: dict[str, str] = {
    'ru': '✅ Авторизация прошла успешно!',
    'en': '✅ Authorization was successful!'
}

ERROR: dict[str, str] = {
    'ru': '❗️Ошибка.\n'
          'Попробуйте позже.',
    'en': '❗️Error.\n'
          'Try later.'
}

CREATE_SESSION_TOKEN_MENU: dict[str, dict[str, str]] = {
    'ru': {
        'create_token': 'Создать токен',
        'back': '<< Назад'
    },
    'en': {
        'create_token': 'Create token',
        'back': '<< Back'
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

INPUT_LOGIN_TEXT: dict[str, str] = {
    'ru': 'Введите имя вашего персонажа на сервере.',
    'en': 'Enter the name of your character on the server.'
}

INPUT_PASSWORD_TEXT: dict[str, str] = {
    'ru': 'Введите пароль, который используется для входа в игру этим персонажем.',
    'en': 'Enter the password that is used to enter the game by this character.'
}

TOKEN_CREATE_403: dict[str, str] = {
    'ru': '❗️Возможно, имя пользователя или пароль неверны, или эта учетная запись не имеет достаточных привилегий.',
    'en': '❗️Username or password may be incorrect or this account may not have sufficient privileges.'
}

TOKEN_CREATE_200: dict[str, str] = {
    'ru': '✅ Токен создан!\n'
          'Авторизация прошла успешно!\n'
          'Созданный токен можно будет получить в разделе "Токены".',
    'en': '✅ Token created!\n'
          'Authorization was successful!\n'
          'The created token can be obtained in the "Tokens" section.'
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

MAIN_MENU_TEXT: dict[str, str] = {
    'ru': '📜 Главное меню',
    'en': '📜 Main menu'
}
