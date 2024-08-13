from aiogram import types, Router, F
from aiogram.filters import Command, CommandStart
from keyboards import reply, inline

# from aiogram.fsm.context import FSMContext

user_dp = Router()


@user_dp.message(CommandStart())
async def start_handler(message: types.Message):
    # print(message)
    await message.answer(f"Counter: 0", reply_markup=await inline.call_markup(counter=0))


@user_dp.message(Command('help'))
async def help_handler(message: types.Message):
    await message.answer(
        'help',
        reply_markup=await inline.help_inline_markup()
    )


@user_dp.message(Command('admin'), F.from_user.id == 2124744962)
async def echo(message: types.Message):
    return await message.answer(message.text, reply_markup=await inline.send_inline_markup())


@user_dp.callback_query(F.data.startswith('counter'))
async def counter(callback: types.CallbackQuery):
    print(f'\n{callback.data = }\n')
    print(callback.data.split('_'))

    _, counter = callback.data.split('_')

    await callback.message.edit_text(
        f'Counter: {counter}',
        reply_markup=await inline.call_markup(int(counter))
    )


@user_dp.callback_query()
async def help_callback(callback: types.CallbackQuery):

    await callback.message.edit_text(
        f'Help callback is works',
    )

# @user_dp.message(F.text == "salom")
# async def answer_to(message: types.Message):
#
#     await message.answer(
#         'Senga ham salom',
#         reply_markup=await reply.help_markup()
#
#     )
#
#
# @user_dp.message(Command('info'))
# async def get_user_info(message: types.Message):
#     await message.answer(
#         'Ma\'lumoptlarizni kiriting.',
#         reply_markup=await reply.get_user_contact()
#     )
#
#
# @user_dp.message()
# async def get_info(message: types.Message):
#     await message.answer(
#         'Qabul qilindi',
#         reply_markup=await reply.remove_markup()
#     )
