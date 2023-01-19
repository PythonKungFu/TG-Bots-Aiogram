from aiogram import Bot, Dispatcher, executor, types
from config import TOKEN


# Define Bot, Dispatcher
bot: Bot = Bot(token=TOKEN)
dp: Dispatcher = Dispatcher(bot)


# Handler /start
async def process_start_command(message: types.Message):
    await message.answer('Привет!\nМеня зовут Эхо-бот!\nНапиши мне что-нибудь')


# Handler /help
async def process_help_command(message: types.Message):
    await message.answer('Напиши мне что-нибудь и в ответ я пришлю тебе твое сообщение')


# Handler any message
async def send_echo(message: types.Message):
    await message.reply(message.text)


# Register handlers in dispatcher
dp.register_message_handler(process_start_command, commands=['start'])
dp.register_message_handler(process_help_command, commands=['help'])
dp.register_message_handler(send_echo)


# if __main__
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
