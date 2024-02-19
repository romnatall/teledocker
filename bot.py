import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
#from aiologger import Logger
import dic

with open('token.txt', 'r') as file:
    bot = Bot(token=file.read().strip())

dp = Dispatcher()

logging.basicConfig(
    level=logging.INFO, 
    filename = r"mflog.log", 
    #format = "%(asctime)s - %(module)s - %(levelname)s - %(funcName)s: %(lineno)d - %(message)s", 
    datefmt='%H:%M:%S',
    )


@dp.message()
async def echo(message: types.Message):
    logging.info(message.text+" "+ message.from_user.username)
    text = message.text.upper()
    d=dic.transliteration_dict
    ans=''.join([d[i] if i in d.keys() else i for i in text])
    await message.reply(ans)

logging.info("логим1")
async def main():
    logging.info("логим")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
