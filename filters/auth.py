from aiogram.filters import BaseFilter
from aiogram.types import Message
from sqlalchemy.ext.asyncio import AsyncSession

from models.methods import get_userdata
from models.models import User
from services.api_requests import tokentest


class IsAuth(BaseFilter):
    async def __call__(self, message: Message, session: AsyncSession) -> bool:
        user_data:  User | None = await get_userdata(session, message.from_user.id)
        if not user_data:
            return False

        token_test_result: dict = await tokentest(user_data.api_token)

        return True if token_test_result['status'] == '200' else False
