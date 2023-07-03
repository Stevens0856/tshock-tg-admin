SERVER_SECTION_MENU_TEXT: dict[str, str] = {
    'ru': '⚙️ <b>Сервер</b>',
    'en': '⚙️ <b>Server</b>'
}

WAITING_BROADCAST_INPUT: dict[str, str] = {
    'ru': '⌨️ Введите текст сообщения для рассылки.',
    'en': '⌨️ Enter the text of the message to send.'
}

WAITING_RAW_CMD_INPUT: dict[str, str] = {
    'ru': '⌨️ Введите команду, которую хотите выполнить.',
    'en': '⌨️ Enter the command you want to run.'
}

SERVER_STATUS: dict[str, str] = {
    'ru': '🔋 <b>Статус сервера</b>\n\n'
          'ℹ️ Имя: {name}\n'
          '🎮 Версия игры: <code>{serverversion}</code>\n'
          '🔧 Версия TShock: <code>{tshockversion}</code>\n'
          '⚙️ Порт: {port}\n'
          '🟢 Онлайн: {playercount}\n'
          '👫 Вместимость: {maxplayers}\n'
          '🌎 Мир: {world}\n'
          '🕰 Аптайм: {uptime}\n'
          '🔐 Пароль сервера: {serverpassword}',
    'en': '🔋 <b>Server status</b>\n\n'
          'ℹ️ Name: {name}\n'
          '🎮 Game version: <code>{serverversion}</code>\n'
          '🔧 TShock version: <code>{tshockversion}</code>\n'
          '⚙️ Port: {port}\n'
          '🟢 Online: {playercount}\n'
          '👫 Capacity: {maxplayers}\n'
          '🌎 World: {world}\n'
          '🕰 Uptime: {uptime}\n'
          '🔐 Server password: {serverpassword}'
}

WORLD_READ: dict[str, str] = {
    'ru': '🌎 <b>Информация о мире</b>\n\n'
          'ℹ️ Имя: {name}\n'
          '🗺 Размер: {size}\n'
          '🌅 Время суток: {time_of_day}\n'
          '⏱ Время суток длится уже: {time}\n'
          '🌚 Кровавая луна: {bloodmoon}\n'
          '⚔️ Размер вторжения: {invasionsize}',
    'en': '🌎 <b>World information</b>\n\n'
          'ℹ️ Name: {name}\n'
          '🗺 Size: {size}\n'
          '🌅 Time of day: {time_of_day}\n'
          '⏱ Time of day lasts already: {time}\n'
          '🌚 Bloodmoon: {bloodmoon}\n'
          '⚔️ Invasion size: {invasionsize}'
}

SERVER_PASSWORD_FALSE: dict[str, str] = {
    'ru': 'не установлен',
    'en': 'not set'
}

TIME_OF_DAY: dict[str, dict[str, str]] = {
    'ru': {
        'day': 'день',
        'night': 'ночь'
    },
    'en': {
        'day': 'day',
        'night': 'night'
    }
}

BROADCAST_200: dict[str, str] = {
    'ru': '🔊 Сообщение успешно передано.',
    'en': '🔊 The message was broadcasted successfully.'
}

RAW_CMD_200: dict[str, str] = {
    'ru': '⬇️ Результат:\n',
    'en': '⬇️ Result:\n'
}
