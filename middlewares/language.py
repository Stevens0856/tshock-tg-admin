from typing import Any, Dict, Callable, Awaitable

from aiogram import BaseMiddleware
from aiogram.types import TelegramObject

from models.methods import get_language


class UserLanguageMiddleware(BaseMiddleware):
    async def __call__(
            self,
            handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
            event: TelegramObject,
            data: Dict[str, Any],
    ) -> Any:
        try:
            user_id = data['event_from_user'].id
        except KeyError:
            data["language"] = 'en'
            return await handler(event, data)

        language = await get_language(data["session"], user_id)
        data["language"] = language if language else 'en'

        return await handler(event, data)
