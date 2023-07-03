import logging
from typing import Any, Dict, Callable, Awaitable

from aiogram import BaseMiddleware
from aiogram.types import TelegramObject

from lexicon.default.message_texts import CONNECTION_ERROR, TOKEN_EXPIRED
from models.models import User
from services.api_requests import tokentest

log: logging.Logger = logging.getLogger('token_test')


class TokenTestMiddleware(BaseMiddleware):
    async def __call__(
            self,
            handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
            event: TelegramObject,
            data: Dict[str, Any],
    ) -> Any:
        user: User = data["user_data"]
        if not user:
            return await handler(event, data)

        token_test_result: dict = await tokentest(user.api_token)
        # If there is no connection at each event, we notify the user about this.
        if token_test_result['status'] == 'error':
            await event.answer(text=CONNECTION_ERROR[data["language"]])
        # We just notify the user about the expired token. He can re-release it himself.
        elif token_test_result['status'] == '403':
            await event.answer(text=TOKEN_EXPIRED[data["language"]])

        return await handler(event, data)
