from aiogram import Bot, Dispatcher, executor, types
from git import git_url
from aiogram.dispatcher.filters import Text
from API import config
import logging




bot = Bot(token=config.bot_token.get_secret_value())

dp = Dispatcher(bot)

logging.basicConfig(level=logging.INFO)
logging.basicConfig(level=logging.DEBUG)
logging.basicConfig(level=logging.ERROR)


#Информация о нас и приветствие
@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Привет!\nНас зовут Влад и Дмитрий\nНе переживай с тобой мы уже знакомы))\nВ данном боте ты сможешь узнать про наши git репозитории\nНапиши '/link' и будь с нами в одной команде. \nНаши Соц. сети: /soc")

#кейборд с нашыми репами
@dp.message_handler(commands=['link'])
async def link(message: types.Message):
    keybord=types.ReplyKeyboardMarkup(resize_keyboard=True)
    but = ['Первые тестовые софты для stepik']
    keybord.add(*but)
    await message.answer('Выбери репозиторий', reply_markup=keybord)

@dp.message_handler(commands=['soc'])
async def link(message: types.Message):
    but = ['Ссылки на наши Соц. Сети']
    await message.answer('Я')
    await message.answer(git_url[1])
    await message.answer('Дима')
    await message.answer(git_url[2])

#вывод первой ноши репы
@dp.message_handler(Text(equals='Первые тестовые софты для stepik'))
async def cod_1(message: types.Message):
    await message.reply('Отличный выбор. Вот твой репозиторий:', reply_markup=types.ReplyKeyboardRemove())
    await message.reply(git_url[0])

@dp.message_handler(Text(equals='Ссылки на Соц. Сети'))
async def cod_2(message: types.Message):
    await message.answer('Я', reply_markup=types.ReplyKeyboardRemove())
    await message.answer(git_url[1])
    await message.answer('Дима', reply_markup=types.ReplyKeyboardRemove())
    await message.answer(git_url[2])



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)