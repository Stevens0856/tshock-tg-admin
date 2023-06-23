from aiogram.filters import BaseFilter
from aiogram.types import Message
from sqlalchemy.ext.asyncio import AsyncSession

from models.methods import get_userdata
from models.models import User


class IsAuth(BaseFilter):
    async def __call__(self, message: Message, session: AsyncSession) -> bool:
        user_data:  User | None = await get_userdata(session, message.from_user.id)
        return True if user_data else False
