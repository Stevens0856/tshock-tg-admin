from lexicon.default.message_texts import TIME, ACTIVITY_STATUS
from lexicon.server_section.message_texts import SERVER_STATUS, SERVER_PASSWORD_FALSE, TIME_OF_DAY, WORLD_READ


def convert_uptime_to_humanreadable(uptime: str, lang: str) -> str:
    days, time = uptime.split('.')
    hours, minutes, seconds = time.split(':')

    result: str = ''
    if int(days) > 0:
        result += f'{days}{TIME[lang]["d"]}'

    if int(hours) > 0:
        result += f'{hours}{TIME[lang]["h"]}'

    if int(minutes) > 0:
        result += f'{minutes}{TIME[lang]["m"]}'

    if int(seconds) > 0:
        result += f'{seconds}{TIME[lang]["s"]}'

    return result


def convert_time(time_in_seconds: float, lang: str) -> str:
    int_time_in_seconds: int = int(time_in_seconds)
    shifted_time: int = int_time_in_seconds + 4 * 3600 + 30 * 60

    total_minutes: int = int(shifted_time / 60)
    hours: int = total_minutes // 60
    minutes: int = total_minutes % 60
    seconds: int = int_time_in_seconds % 60

    if hours >= 24:
        hours -= 24

    time_string: str = f'{hours}{TIME[lang]["h"]}{minutes}{TIME[lang]["m"]}{seconds}{TIME[lang]["s"]}'
    return time_string


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


def convert_world_read_response_to_message(response: dict, lang: str) -> str:
    time: str = convert_time(response['time'], lang)
    time_of_day: str = TIME_OF_DAY[lang]['day'] if response['daytime'] else TIME_OF_DAY[lang]['night']
    bloodmoon: str = ACTIVITY_STATUS[lang][True] if response['bloodmoon'] else ACTIVITY_STATUS[lang][False]
    message: str = WORLD_READ[lang].format(name=response['name'],
                                           size=response['size'],
                                           time=time,
                                           time_of_day=time_of_day,
                                           bloodmoon=bloodmoon,
                                           invasionsize=response['invasionsize'])
    return message
