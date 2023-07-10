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


def convert_time_to_humanreadable(response_time: float, lang: str) -> str:
    seconds: int = int(response_time)
    result: str = ''

    hours: int = seconds // 3600
    minutes: int = (seconds // 60) % 60
    seconds: int = seconds % 60

    if hours > 0:
        result += f'{hours}{TIME[lang]["h"]}'

    if minutes > 0:
        result += f'{minutes}{TIME[lang]["m"]}'

    if seconds > 0:
        result += f'{seconds}{TIME[lang]["s"]}'

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


def convert_world_read_response_to_message(response: dict, lang: str) -> str:
    time: str = convert_time_to_humanreadable(response['time'], lang)
    time_of_day: str = TIME_OF_DAY[lang]['day'] if response['daytime'] else TIME_OF_DAY[lang]['night']
    bloodmoon: str = ACTIVITY_STATUS[lang][True] if response['bloodmoon'] else ACTIVITY_STATUS[lang][False]
    message: str = WORLD_READ[lang].format(name=response['name'],
                                           size=response['size'],
                                           time=time,
                                           time_of_day=time_of_day,
                                           bloodmoon=bloodmoon,
                                           invasionsize=response['invasionsize'])
    return message


def convert_raw_cmd_response_to_message(response: list[str], lang: str) -> str:
    message: str = RAW_CMD_200[lang]
    for line in response:
        message += line + '\n'

    # Fix HTML style markup constraint
    message = message.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')

    return message


class AllUsers:
    def __init__(self, all_users: list, page_size: int = 5):
        self.user_list = all_users
        self.page_size = page_size
        self.page_count: int = math.ceil(len(all_users) / self.page_size)

    def get_page_data(self, current_page: int) -> list:
        start: int = (current_page - 1) * self.page_size
        end: int = start + self.page_size

        return self.user_list[start:min(end, len(self.user_list))]

    def get_target_page(self, action: str, current_page: int) -> int:
        target_page: int = current_page
        match action:
            case 'backward':
                if current_page > 1:
                    target_page -= 1
            case 'forward':
                if current_page < self.page_count:
                    target_page += 1
            case 'start_page':
                target_page = 1
            case 'last_page':
                target_page = self.page_count

        return min(target_page, self.page_count)


class ActiveUsers(AllUsers):
    def __init__(self, active_users_response: str, page_size: int = 5):
        self.active_users_response = active_users_response
        self.page_size = page_size
        self.user_list, self.page_count = self._parse_active_users()

    def _parse_active_users(self) -> tuple[list[str], int]:
        nicknames = self.active_users_response.split('\t')
        active_users = [nickname for nickname in nicknames if nickname]
        page_count: int = math.ceil(len(active_users) / self.page_size)
        return active_users, page_count
