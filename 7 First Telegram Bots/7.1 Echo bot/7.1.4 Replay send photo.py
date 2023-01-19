from aiogram import Bot, Dispatcher, executor, types
from config import TOKEN
from pprint import pp


# Define Bot, Dispatcher
bot: Bot = Bot(token=TOKEN)
dp: Dispatcher = Dispatcher(bot)


# Handler /start
async def process_start_command(message: types.Message):
    await message.answer('Привет!\nМеня зовут Эхо-бот!\nНапиши мне что-нибудь')


# handler /help
async def process_help_command(message: types.Message):
    await message.answer('Напиши мне что-нибудь и в ответ я пришлю тебе твое сообщение')


# handler photo
async def send_photo_echo(message: types.Message):
    await message.reply_photo(message.photo[0].file_id)


# handler sticker
async def send_sticker_echo(message: types.Message):
    await message.reply_sticker(message.sticker.file_id)


# handler document
async def send_document_echo(message: types.Message):
    await message.reply_document(message.document.file_id)


# handler any message
async def send_echo(message: types.Message):
    await message.reply(message.text)


# register handlers in dispatcher
dp.register_message_handler(process_start_command, commands=['start'])
dp.register_message_handler(process_help_command, commands=['help'])
dp.register_message_handler(send_photo_echo, content_types=['photo'])
dp.register_message_handler(send_sticker_echo, content_types=['sticker'])
dp.register_message_handler(send_document_echo, content_types=['document'])
dp.register_message_handler(send_echo)


# if __name__
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
