from aiogram.filters.callback_data import CallbackData


class PaginationCallbackFactory(CallbackData, prefix="pagination"):
    action: str


class ActiveUsersCallbackFactory(CallbackData, prefix="active_users", sep='<<$;&^!|>>//'):
    username: str
