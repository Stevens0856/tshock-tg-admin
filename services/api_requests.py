import logging

import aiohttp
from aiohttp import ClientConnectorError

from config.configreader import config


log = logging.getLogger('api_requests')


async def request(endpoint: str, token: str = '', **kwargs) -> dict:
    url: str = f"http://{config.tshock_server_host}:{config.tshock_server_port}/{endpoint}"
    params: dict = {"token": token, **kwargs}

    for key, value in kwargs.items():
        params[key] = str(value)

    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(url, params=params, timeout=5) as response:
                data: dict = await response.json()
                return data
        except ClientConnectorError as e:
            log.error(f"request | Exception: {e}")
            return {'status': 'error'}


async def tokentest(token: str) -> dict:
    """
    /tokentest

    Description:

    Tests the token to see if it is valid

    Returns:

    data - A response json-message

    :param token: Server token
    :return: a result dict
    """

    return await request("tokentest", token)


async def v2_token_create(username: str, password: str) -> dict:
    """
    /v2/token/create

    Description:

    Creates an authenticated token for use with other endpoints

    Returns:

    HTTP 200 if the authentication succeeds

    HTTP 403 if the authentication fails

    response - Error message if the authentication failed, else an authenticated token.

    :param username: User with which to authenticate the token
    :param password: User's password
    :return: a result dict
    """

    return await request("v2/token/create", username=username, password=password)


async def v2_server_status(token: str, players: bool = False, rules: bool = False) -> dict:
    """
    /v2/server/status

    Description:

    Prints out details about the status of the currently running server

    Returns:

    name - Server name

    port - Port the server is running on

    playercount - Number of players currently online

    maxplayers - The maximum number of players the server support

    world - The name of the currently running world

    players - (optional) an array of players including the following information: nickname, username, ip, group, active, state, team

    rules - (optional) an array of server rules which are name value pairs e.g. AutoSave, DisableBuild etc

    :param token: Server token
    :param players: A bool value indicating if the status response should include player information
    :param rules: A bool value indicating if the status response should include rule information
    :return: a result dict
    """
    return await request("v2/server/status", token, players=players, rules=rules)


async def world_read(token: str):
    """
    Description:

    Get information regarding the world. No special permissions are required for this route.

    Returns:

    name - The name of the world.

    size - The size of the world.

    time - The time of the world.

    daytime - Whether or not it is daytime.

    bloodmoon - The bloodmoon status of the world.

    invasionsize - The invasion size of the world.

    :param token: Server token
    :return: a result dict
    """
    return await request("world/read", token)


async def v3_server_rawcmd(token: str, cmd: str) -> dict:
    """
    Description:

    Issues a raw command on the server just as if you typed it into the console.

    Returns:

    response - The response from the executed command User Commands

    :param token: Server token
    :param cmd: The command to execute on the server
    :return: a result dict
    """
    return await request("v3/server/rawcmd", token, cmd=cmd)


async def v2_server_broadcast(token: str, msg: str) -> dict:
    """
    /v2/server/broadcast

    Description:

    Performs a server broadcast to all players on the server

    Returns:

    response - A response message

    :param token: Server token
    :param msg: The message to broadcast
    :return: a result dict
    """
    return await request("v2/server/broadcast", token, msg=msg)


async def v2_users_activelist(token: str) -> dict:
    """
    Description:

    Returns a list of currently active users on the server

    Returns:

    activeusers - List of active users separated by a tab character

    :param token: Server token
    :return: a result dict
    """
    return await request("v2/users/activelist", token)


async def v2_users_list(token: str):
    """
    Description:

    Lists all user accounts in the TShock database.

    Returns:

    users - A list of all users in the TShock database.

    :param token: Server token
    :return: a result dict
    """
    return await request("v2/users/list", token)
