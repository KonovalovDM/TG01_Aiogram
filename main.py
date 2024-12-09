import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

from config import TOKEN

import random

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command('photo'))
async def photo(message: Message):
    list = ['http://cdn.fishki.net/upload/post/201508/06/1619927/3_2.jpg', 'http://cdn.fishki.net/upload/post/201508/06/1619927/4_4.jpg', 'http://cdn.fishki.net/upload/post/201508/06/1619927/4_1.jpg', 'http://cdn.fishki.net/upload/post/201508/06/1619927/3_3.jpg', 'http://cdn.fishki.net/upload/post/201508/06/1619927/3_6.jpg', 'http://cdn.fishki.net/upload/post/201508/06/1619927/26.jpg']
    rand_photo = random.choice(list)
    await message.answer_photo(photo=rand_photo, caption='это крутая фотка')


@dp.message(F.photo)
async def react_photo(message: Message):
    list = ['Ого, какая непонятная фотка!', 'Непонятно, что это такое?!', 'Не отправляй мне Такое больше!']
    rand_answ = random.choice(list)
    await message.answer(rand_answ)

@dp.message(F.text == "Что такое ИИ?")
async def aitext(message: Message):
    await message.answer('Иску́сственный интелле́кт (англ. artificial intelligence; AI) в самом широком смысле — это интеллект, демонстрируемый машинами, в частности компьютерными системами. Это область исследований в области компьютерных наук, которая разрабатывает и изучает методы и программное обеспечение, позволяющие машинам воспринимать окружающую среду и использовать обучение и интеллект для выполнения действий, которые максимально увеличивают их шансы на достижение поставленных целей. Такие машины можно назвать искусственным интеллектом. ')



@dp.message(Command('help'))
async def help(message: Message):
    await message.answer('Этот бот умеет выполнять команды: \n /start \n /help')

@dp.message(CommandStart)
async def start(message: Message):
    await message.answer('Приветики! Я бот!')


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
