from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from aiogram.utils.keyboard import ReplyKeyboardBuilder


async def start_markup():
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text='hello'),
                KeyboardButton(text='world'),

            ],
            [
                KeyboardButton(text='hello2'),
                KeyboardButton(text='hello3'),
            ],
            [
                KeyboardButton(text='hello2'),
                KeyboardButton(text='hello3'),
            ],
        ],
        resize_keyboard=True,
        one_time_keyboard=True,
        input_field_placeholder='Tuglmalardan birini tanlang.'
    )
    return keyboard


async def generate_markup(buttons: list):
    builder = ReplyKeyboardBuilder()

    for button in buttons:
        builder.add(
            KeyboardButton(text=button)
        )
    builder.adjust(*(2,))

    # builder2 = ReplyKeyboardBuilder()
    # builder2.add(
    #     KeyboardButton(text='back'),
    #     KeyboardButton(text='back2'),
    #     KeyboardButton(text='back3')
    # )
    # builder2.adjust(*(3,))
    #
    # builder.attach(builder2)

    return builder.as_markup(
        resize_keyboard=True
    )


async def generate(buttons, sizes=(1,)):
    builder = ReplyKeyboardBuilder()
    for button in buttons:
        builder.add(
            KeyboardButton(text=button)
        )
    builder.adjust(*sizes)
    return builder


async def help_markup():
    buttons = ['1', '2', '3']
    keyword = await generate(buttons, (2,))
    return keyword.as_markup(one_time_keyboard=True)


async def get_user_contact():
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text='Send contact', request_contact=True)],
            [KeyboardButton(text='Send location', request_location=True)],
        ],
        resize_keyboard=True
    )

    return keyboard


async def remove_markup():
    return ReplyKeyboardRemove()
