from aiogram import types, Router, F
from aiogram.filters import Command, CommandStart

# from aiogram.fsm.context import FSMContext

user_dp = Router()


@user_dp.message(CommandStart())
async def start_handler(message: types.Message):
    print(message)
    await message.answer("Hello wolrd")
    await message.reply("hello")


@user_dp.message(F.text == "salom")
async def answer_to(message: types.Message):

    await message.answer('Senga ham salom')







