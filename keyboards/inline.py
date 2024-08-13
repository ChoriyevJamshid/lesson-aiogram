from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


async def call_markup(counter: int):

    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            # [InlineKeyboardButton(text='Orifjon aka', url='https://t.me/orifjon_0987')],
            [
                InlineKeyboardButton(text=' + ', callback_data=f'counter_{counter + 1}'), #counter_-1
                InlineKeyboardButton(text=' - ', callback_data=f'counter_{counter - 1}')
            ]
        ]
    )

    return keyboard


async def help_inline_markup():
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            # [InlineKeyboardButton(text='Orifjon aka', url='https://t.me/orifjon_0987')],
            [
                InlineKeyboardButton(text='Help', callback_data=f'help')
            ]
        ]
    )

    return keyboard


async def send_inline_markup():
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            # [InlineKeyboardButton(text='Orifjon aka', url='https://t.me/orifjon_0987')],
            [
                InlineKeyboardButton(text='Send', callback_data=f'send')
            ]
        ]
    )

    return keyboard
