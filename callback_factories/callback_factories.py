from aiogram.filters.callback_data import CallbackData


class PaginationCallbackFactory(CallbackData, prefix="pagination"):
    action: str


class ActiveUsersCallbackFactory(CallbackData, prefix="active_users", sep='_$&'):
    username: str


class AllUsersCallbackFactory(CallbackData, prefix="all_users", sep='_$&'):
    id: int
    username: str
    group: str


class AllUsersHeaderCallbackFactory(CallbackData, prefix="all_users_header", sep='_$&'):
    header: str
