from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from models.base import metadata
from models.models import User


async def create_tables(engine):
    async with engine.begin() as conn:
        await conn.run_sync(metadata.create_all)


async def get_userdata(session: AsyncSession, telegram_id: int) -> User | None:
    user_data_request = await session.execute(
        select(User).where(User.user_id == telegram_id)
    )
    return user_data_request.scalars().one_or_none()
