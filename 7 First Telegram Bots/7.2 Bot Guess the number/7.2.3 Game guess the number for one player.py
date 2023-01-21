from aiogram import Bot, Dispatcher, executor
from aiogram.types import Message
from aiogram.dispatcher.filters import Text
from config import TOKEN
import random


# Создаем объекты бота и диспетчера
bot: Bot = Bot(token=TOKEN)
dp: Dispatcher = Dispatcher(bot)

# Количество попыток доступных пользователю в игре
ATTEMPTS: int = 5

# Словарь в котором будут храниться данные пользователя
user: dict = {
    'in_game': False,
    'secret_number': None,
    'attempts': None,
    'total_games': 0,
    'wins': 0
}


# Функция возвращающая случайное число от 1 до 100
def get_random_number() -> int:
    return random.randint(1, 100)


# Этот хэндлер будет срабатывать на команду /start
async def process_start_command(message: Message):
    await message.answer('Привет!\nДавай сыграем в игру "Угадай число"?\n\nЧтобы получить правила игры и '
                         'список доступных команд - отправьте команду /help')


# Этот хэндлер будет срабатывать на команду /help
async def process_help_command(message: Message):
    await message.answer(f'Правила игры:\n\nЯ загадываю число от 1 до 100, а вам нужно его угадать\n'
                         f'У вас есть {ATTEMPTS} попыток\n\nДоступные команды:\n/help - правила игры и список команд\n'
                         f'/cancel - выйти из игры\n/stat - посмотреть статистику\n\nДавай сыграем?')


# Этот хэндлер будет срабатывать на команду /stat
async def process_stat_command(message: Message):
    await message.answer(f'Всего игр сыграно: {user["total_games"]}\nИгр выиграно: {user["wins"]}')


# Этот хэндлер будет срабатывать на команду /cancel
async def process_cancel_command(message: Message):
    if user['in_game']:
        await message.answer('Вы вышли из игры. Если захотите сыграть снова - напишите об этом')
        user['in_game'] = False
    else:
        await message.answer('А мы итак с вами не играем. Может, сыграем разок?')


# Этот хэндлер будет срабатывать на согласие пользователя сыграть в игру
async def process_positive_answer(message: Message):
    if not user['in_game']:
        await message.answer(f'Ура!\n\nЯ загадал число от 1 до 100, попробуй угадать!'
                             f'\nКоличество попыток: {ATTEMPTS}')
        user['in_game'] = True
        user['secret_number'] = get_random_number()
        user['attempts'] = ATTEMPTS
    else:
        await message.answer('Пока мы играем в игру я могу реагировать только на числа от 1 до 100'
                             ' и команды /cancel и /stat')


# Этот хэндлер будет срабатывать на отказ пользователя сыграть в игру
async def process_negative_answer(message: Message):
    if not user['in_game']:
        await message.answer('Жаль :(\n\nЕсли захотите поиграть - просто напишите об этом')
    else:
        await message.answer('Мы же сейчас с вами играем. Присылайте, пожалуйста, числа от 1 до 100')


# Этот хэндлер будет срабатывать на отправку пользователем чисел от 1 до 100
async def process_number_answers(message: Message):
    if user['in_game']:
        if int(message.text) == user['secret_number']:
            await message.answer('Ура!!! Вы угадали число!\n\nМожет, сыграем еще?')
            user['in_game'] = False
            user['total_games'] += 1
            user['wins'] += 1
        elif int(message.text) > user['secret_number']:
            user['attempts'] -= 1
            await message.answer(f'Мое число меньше\nКоличество попыток осталось: {user["attempts"]}')
        elif int(message.text) < user['secret_number']:
            user['attempts'] -= 1
            await message.answer(f'Мое число больше\nКоличество попыток осталось: {user["attempts"]}')

        if user['attempts'] == 0:
            await message.answer(f'К сожалению, у вас больше не осталось попыток. Вы проиграли :(\n\n'
                                 f'Мое число было {user["secret_number"]}\n\nДавайте сыграем еще?')
            user['in_game'] = False
            user['total_games'] += 1
    else:
        await message.answer('Мы еще не играем. Хотите сыграть?')


# Этот хэндлер будет обрабатывать остальные текстовые сообщения
async def process_other_text_answers(message: Message):
    if user['in_game']:
        await message.answer('Мы же сейчас с вами играем. Присылайте, пожалуйста, числа от 1 до 100')
    else:
        await message.answer('Я довольно ограниченный бот, давайте просто сыграем в игру?')


# Регистрация хэндлеров
dp.register_message_handler(process_start_command, commands=['start'])
dp.register_message_handler(process_help_command, commands=['help'])
dp.register_message_handler(process_stat_command, commands=['stat'])
dp.register_message_handler(process_cancel_command, commands=['cancel'])
dp.register_message_handler(process_positive_answer, Text(equals=['Да', 'Давай', 'Сыграем', 'Игра', 'Играть',
                                                                  'Хочу играть'], ignore_case=True))
dp.register_message_handler(process_negative_answer, Text(equals=['Нет', 'Не', 'Не хочу'], ignore_case=True))
dp.register_message_handler(process_number_answers, lambda x: x.text.isdigit() and 1 <= int(x.text) <= 100)
dp.register_message_handler(process_other_text_answers)


# Точка входа
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
