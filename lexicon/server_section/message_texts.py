SERVER_SECTION_MENU_TEXT: dict[str, str] = {
    'ru': 'Раздел <b>Сервер</b>',
    'en': '<b>Server</b> section'
}

WAITING_BROADCAST_INPUT: dict[str, str] = {
    'ru': 'Введите текст сообщения для рассылки.',
    'en': 'Enter the text of the message to send.'
}

WAITING_RAW_CMD_INPUT: dict[str, str] = {
    'ru': 'Введите команду, которую хотите выполнить.',
    'en': 'Enter the command you want to run.'
}

SERVER_STATUS: dict[str, str] = {
    'ru': 'Имя сервера: {name}\n'
          'Версия сервера: <code>{serverversion}</code>\n'
          'Версия TShock: <code>{tshockversion}</code>\n'
          'Порт: {port}\n'
          'Количество игроков онлайн: {playercount}\n'
          'Максимальная вместимость игроков: {maxplayers}\n'
          'Мир: {world}\n'
          'Аптайм: {uptime}\n'
          'Пароль сервера: {serverpassword}\n',
    'en': 'Server name: {name}\n'
          'Server version: {serverversion}\n'
          'TShock version: {tshockversion}\n'
          'Port: {port}\n'
          'Number of players online: {playercount}\n'
          'Maximum players capacity: {maxplayers}\n'
          'World: {world}\n'
          'Uptime: {uptime}\n'
          'Server password: {serverpassword}\n'
}

SERVER_PASSWORD_FALSE: dict[str, str] = {
    'ru': 'Не установлен',
    'en': 'Not set'
}

UPTIME: dict[str, dict[str, str]] = {
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
