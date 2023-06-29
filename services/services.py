from lexicon.server_section.message_texts import SERVER_STATUS, SERVER_PASSWORD_FALSE, UPTIME


def convert_uptime_to_humanreadable(uptime: str, lang: str) -> str:
    days, time = uptime.split('.')
    hours, minutes, seconds = time.split(':')

    result: str = ''
    if int(days) > 0:
        result += f'{days}{UPTIME[lang]["d"]}'

    if int(hours) > 0:
        result += f'{hours}{UPTIME[lang]["h"]}'

    if int(minutes) > 0:
        result += f'{minutes}{UPTIME[lang]["m"]}'

    if int(seconds) > 0:
        result += f'{seconds}{UPTIME[lang]["s"]}'

    return result


def convert_server_status_response_to_message(response: dict, lang: str) -> str:
    server_password: str = response['serverpassword'] if response['serverpassword'] else SERVER_PASSWORD_FALSE[lang]
    uptime: str = convert_uptime_to_humanreadable(response['uptime'], lang)
    message: str = SERVER_STATUS[lang].format(name=response['name'],
                                              serverversion=response['serverversion'],
                                              tshockversion=response['tshockversion'],
                                              port=response['port'],
                                              playercount=response['playercount'],
                                              maxplayers=response['maxplayers'],
                                              world=response['world'],
                                              uptime=uptime,
                                              serverpassword=server_password)
    return message
