# Import
from aiogram import Bot, Dispatcher, executor
from aiogram.types import Message
from aiogram.dispatcher.filters import Text
from config import TOKEN
from dataclasses import dataclass
import random
from typing import Dict


# Define bot
bot: Bot = Bot(token=TOKEN)
dp: Dispatcher = Dispatcher(bot)


# Init class user -> in_game, attempts, total_games, wins, secret number
@dataclass
class User:
    in_game: bool = False
    secret_numbers: int = 0
    attempts: int = 7
    total_games: int = 0
    wins: int = 0


users: Dict[int, User] = {}


# handler /start
async def process_start_command(message: Message):
    if message.from_user.id not in users:
        users[message.from_user.id] = User()
    if users[message.from_user.id].in_game:
        await message.answer('Мы с вами уже играем. Продолжим?')
    else:
        await message.answer(f'Давайте я загадаю число, а вы его попробуете отгадать за '
                             f'{users[message.from_user.id].attempts} попыток?'
                             f'\n\nЧтобы получить правила игры и список доступных команд - отправьте команду /help')


# handler /help
async def process_help_command(message: Message):
    await message.answer(f'Правила игры:\n\n'
                         f'Я загадываю число от 1 до 100, а вам нужно его угадать\n'
                         f'У вас есть {users[message.from_user.id].attempts} попыток\n\n'
                         f'Доступные команды:\n'
                         f'/help - правила игры и список команд\n'
                         f'/cancel - выйти из игры\n'
                         f'/stat - посмотреть статистику\n\nДавай сыграем?')


# handler /stat
async def process_stat_command(message: Message):
    await message.answer(f'Всего игр сыграно: {users[message.from_user.id].total_games}\nИгр выиграно:'
                         f' {users[message.from_user.id].wins}')


# handler /cancel
async def process_cancel_command(message: Message):
    if not users[message.from_user.id].in_game:
        await message.answer('Мы и так не играем. Может все-таки сыграем?')
    else:
        await message.answer('Вы вышли из игры :(. Может все-таки сыграем?')
        users[message.from_user.id].in_game = False


# handler yes_game
async def process_yes_answer(message: Message):
    if users[message.from_user.id].in_game:
        await message.answer('Пока мы играем в игру я могу реагировать только на числа от 1 до 100'
                             ' и команды /cancel и /stat')
    else:
        users[message.from_user.id].in_game = True
        users[message.from_user.id].attempts = 7
        users[message.from_user.id].secret_numbers = random.randint(1, 101)
        await message.answer(f'Ура! Сейчас сыграем!\n'
                             f'Я загадал число от 1 до 100, у вас есть {users[message.from_user.id].attempts}'
                             f' попыток, чтобы угадать.')


# handler no_game
async def process_no_answer(message: Message):
    if not users[message.from_user.id].in_game:
        await message.answer('Мы и так не играем. Может все-таки сыграем?')
    else:
        await message.answer('Вы вышли из игры :(. Может все-таки сыграем?')
        users[message.from_user.id].in_game = False


# handler digit
async def process_digit_message(message: Message):
    if users[message.from_user.id].in_game:
        if int(message.text) > users[message.from_user.id].secret_numbers:
            users[message.from_user.id].attempts -= 1
            await message.answer(f'Загаданное число меньше\n'
                                 f'Осталось {users[message.from_user.id].attempts} попыток!')
        elif int(message.text) == users[message.from_user.id].secret_numbers:
            users[message.from_user.id].in_game = False
            users[message.from_user.id].wins += 1
            users[message.from_user.id].total_games += 1
            await message.answer(f'Ура, вы выиграли!\n'
                                 f'Хотите сыграть еще?')
        elif int(message.text) < users[message.from_user.id].secret_numbers:
            users[message.from_user.id].attempts -= 1
            await message.answer(f'Загаданное число больше\n'
                                 f'Осталось {users[message.from_user.id].attempts} попыток!')
        if users[message.from_user.id].attempts == 0:
            await message.answer('You lose!\nGame again?')
            users[message.from_user.id].in_game = False
            users[message.from_user.id].total_games += 1
    else:
        await message.answer('Давайте сначала начнем игру!')


# handler other message
async def process_other_message(message: Message):
    if users[message.from_user.id].in_game:
        await message.answer('Пишите только цифры!')
    else:
        await message.answer('Я тебя не понимаю! Давай просто сыграем?')


# register handlers
dp.register_message_handler(process_start_command, commands=['start'])
dp.register_message_handler(process_help_command, commands=['help'])
dp.register_message_handler(process_stat_command, commands=['stat'])
dp.register_message_handler(process_cancel_command, commands=['cancel'])
dp.register_message_handler(process_yes_answer, Text(equals=['Да', 'давай', 'ок', 'сыграем', 'игра', 'играть'],
                                                     ignore_case=True))
dp.register_message_handler(process_no_answer, Text(equals=['Нет', 'Не', 'Не хочу', 'Хватит'], ignore_case=True))
dp.register_message_handler(process_digit_message, lambda x: x.text.isdigit() and 1 <= int(x.text) <= 100)
dp.register_message_handler(process_other_message)


# if name
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
