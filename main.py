from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from git import git_url
from aiogram.dispatcher.filters import Text
from pydantic import BaseSettings, SecretStr


from API import config

bot = Bot(token=config.bot_tok.get_secret_value())
dp = Dispatcher(bot)


#Информация о нас и приветствие
@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Привет!\nНас зовут Влад и Дмитрий\nНе переживай с тобой мы уже знакомы))\nВ данном боте ты сможешь узнать про наши git репозитории\nНапиши '/link' и будь снами в одной коомманде")

#кейборд с нашыми репами
@dp.message_handler(commands=['link'])
async def link(message: types.Message):
    keybord=types.ReplyKeyboardMarkup(resize_keyboard=True)
    but = ['Первые тестовые софты для stepik']
    keybord.add(*but)
    await message.answer('Выбери репозиторий', reply_markup=keybord)

#вывод первой ноши репы
@dp.message_handler(Text(equals='Первые тестовые софты для stepik'))
async def cod_1(message: types.Message):
    await message.reply('Отличный выбор. Вот твой репозиторий:', reply_markup=types.ReplyKeyboardRemove())
    await message.reply(git_url[0])



if __name__ == '__main__':
    executor.start_polling(dp)