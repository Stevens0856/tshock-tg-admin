import logging

import aiohttp
from aiohttp import ClientConnectorError

from config.configreader import config


log = logging.getLogger('api_requests')


async def request(endpoint: str, token: str, **kwargs) -> dict:
    url = f"http://{config.tshock_server_host}:{config.tshock_server_port}/{endpoint}"
    params = {"token": token, **kwargs}
    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(url, params=params, timeout=5) as response:
                data = await response.json()
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
