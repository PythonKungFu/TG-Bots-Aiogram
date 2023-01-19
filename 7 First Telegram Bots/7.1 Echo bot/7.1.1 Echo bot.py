from aiogram import Bot, Dispatcher, executor, types
from config import TOKEN


# Define bot, dispatcher
bot: Bot = Bot(token=TOKEN)
dp: Dispatcher = Dispatcher(bot)


# Handler /start
@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.answer('Привет!\nМеня зовут Эхо-бот!\nНапиши мне что-нибудь')


# Handler /help
@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.answer('Напиши мне что-нибудь и в ответ я пришлю тебе твое сообщение')


# Handler message
@dp.message_handler()
async def send_echo(message: types.Message):
    await message.reply(message.text)


# if __name__
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
