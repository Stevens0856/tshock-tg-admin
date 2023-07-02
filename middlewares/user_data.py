from typing import Any, Dict, Callable, Awaitable

from aiogram import BaseMiddleware
from aiogram.types import TelegramObject

from models.methods import get_userdata
from models.models import User


class UserDataMiddleware(BaseMiddleware):
    async def __call__(
            self,
            handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
            event: TelegramObject,
            data: Dict[str, Any],
    ) -> Any:

        data["language"]: str = 'en'
        data["user_data"]: User | None = None

        try:
            user_id: int = data['event_from_user'].id
        except KeyError:
            return await handler(event, data)

        user_data: User | None = await get_userdata(data["session"], user_id)
        if user_data:
            data["user_data"] = user_data
            data["language"] = user_data.lang

        return await handler(event, data)
