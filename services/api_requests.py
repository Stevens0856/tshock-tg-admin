import logging

import aiohttp
from aiohttp import ClientConnectorError

from config.configreader import config


log = logging.getLogger('api_requests')


async def request(endpoint: str, token: str = '', **kwargs) -> dict:
    url: str = f"http://{config.tshock_server_host}:{config.tshock_server_port}/{endpoint}"
    params: dict = {"token": token, **kwargs}
    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(url, params=params, timeout=5) as response:
                data: dict = await response.json()
                return data
        except ClientConnectorError as e:
            log.error(f"request | Exception: {e}")
            return {'status': 'error'}


async def tokentest(token) -> dict:
    """
    /tokentest

    Description:

    Tests the token to see if it is valid

    Returns:

    data - A response json-message

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
