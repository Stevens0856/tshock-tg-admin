WELCOME: str = 'Добро пожаловать! / Welcome!\n' \
               'Выберите язык. / Choose language.'

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
