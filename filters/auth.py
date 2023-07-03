from aiogram.filters import BaseFilter
from aiogram.types import Message

from models.models import User


class IsAuth(BaseFilter):
    async def __call__(self, message: Message, user_data: User | None) -> bool | dict:
        return True if user_data else False
