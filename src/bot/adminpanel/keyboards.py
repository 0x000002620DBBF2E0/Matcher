from aiogram.types import (
    InlineKeyboardMarkup as InlineKeyboard,
    InlineKeyboardButton as InlineButton,
)
from aiogram.utils.keyboard import InlineKeyboardBuilder as InlineBuilder

from bot.adminpanel.enums import AdminAction


def get_admin_actions_buttons() -> InlineKeyboard:
    buttons = [
        InlineButton(
            text="Заблокировать пользователя 👨‍⚖️",
            callback_data=f"admin_action*{AdminAction.ban_user}",
        ),
        InlineButton(
            text="Разблокировать пользователя 🔓",
            callback_data=f"admin_action*{AdminAction.unban_user}",
        ),
    ]
    return buttons


def main_admin_keyboard() -> InlineKeyboard:
    """
    Главная клавиатура админпанели
    """
    builder = InlineBuilder().add(*get_admin_actions_buttons())
    return builder.as_markup()
