import logging
import math

from lexicon.default.message_texts import TIME, ACTIVITY_STATUS
from lexicon.server_section.message_texts import SERVER_STATUS, SERVER_PASSWORD_FALSE, TIME_OF_DAY, WORLD_READ, \
    RAW_CMD_200

log: logging.Logger = logging.getLogger('services')


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


def convert_time(response_time: float, lang: str) -> str:
    seconds = int(response_time)
    hours = seconds // 3600
    minutes = (seconds // 60) % 60
    seconds = seconds % 60

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


def convert_raw_cmd_response_to_message(response: dict, lang: str) -> str:
    message: str = RAW_CMD_200[lang]
    for line in response:
        message += line + '\n'

    return message


class ActiveUsers:
    def __init__(self, active_users_response: str, page_size: int = 5):
        self.active_users_response = active_users_response
        self.page_size = page_size
        self.user_list, self.page_count = self._parse_active_users()

    def _parse_active_users(self) -> tuple[list[str], int]:
        nicknames = self.active_users_response.split('\t')
        active_users = [nickname for nickname in nicknames if nickname]
        page_count: int = math.ceil(len(active_users) / self.page_size)
        return active_users, page_count

    def get_page_data(self, current_page: int) -> list:
        start: int = (current_page - 1) * self.page_size
        end: int = start + self.page_size

        return self.user_list[start:min(end, len(self.user_list))]
