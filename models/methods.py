from contextlib import suppress

from sqlalchemy import select, delete
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from models.base import metadata
from models.models import User


async def create_tables(engine):
    async with engine.begin() as conn:
        await conn.run_sync(metadata.create_all)


async def get_userdata(session: AsyncSession, telegram_id: int) -> User | None:
    result = await session.execute(
        select(User).where(User.user_id == telegram_id)
    )
    return result.scalars().one_or_none()


async def delete_user(session: AsyncSession, telegram_id: int) -> None:
    await session.execute(
        delete(User).where(User.user_id == telegram_id)
    )
    await session.commit()


async def merge_user(session: AsyncSession, telegram_id: int, name_in_game: str, api_token: str, lang: str):
    await session.merge(User(user_id=telegram_id, name_in_game=name_in_game,
                             api_token=api_token, lang=lang))
    # If a user is quick enough, there might be 2 events.
    # There's not much we can do, so simply ignore it until we come up with a better solution
    with suppress(IntegrityError):
        await session.commit()


async def update_lang(session: AsyncSession, telegram_id: int, lang: str) -> None:
    user: User | None = await get_userdata(session, telegram_id)
    if user:
        user.lang = lang
        await session.commit()
    else:
        # Handle the case when the user doesn't exist
        raise ValueError(f"User with telegram_id {telegram_id} does not exist.")
