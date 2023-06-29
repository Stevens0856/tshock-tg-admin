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
          'Пароль сервера: {serverpassword}',
    'en': 'Server name: {name}\n'
          'Server version: <code>{serverversion}</code>\n'
          'TShock version: <code>{tshockversion}</code>\n'
          'Port: {port}\n'
          'Number of players online: {playercount}\n'
          'Maximum players capacity: {maxplayers}\n'
          'World: {world}\n'
          'Uptime: {uptime}\n'
          'Server password: {serverpassword}'
}

WORLD_READ: dict[str, str] = {
    'ru': 'Имя: {name}\n'
          'Размер: {size}\n'
          'Время: {time}\n'
          'Время суток: {time_of_day}\n'
          'Кровавая луна: {bloodmoon}\n'
          'Размер вторжения: {invasionsize}',
    'en': 'Name: {name}\n'
          'Size: {size}\n'
          'Time: {time}\n'
          'Time of day: {time_of_day}\n'
          'Bloodmoon: {bloodmoon}\n'
          'Invasion size: {invasionsize}'
}

SERVER_PASSWORD_FALSE: dict[str, str] = {
    'ru': 'Не установлен',
    'en': 'Not set'
}

TIME_OF_DAY: dict[str, dict[str, str]] = {
    'ru': {
        'day': 'День',
        'night': 'Ночь'
    },
    'en': {
        'day': 'Day',
        'night': 'Night'
    }
}
