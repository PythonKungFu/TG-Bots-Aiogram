from environs import Env


env = Env() # Создаем экземпляр класса Env
env.read_env() # Читаем файл .env и добавляем переменные окружения

bot_token = env('BOT_TOKEN') # Сохраняем значение переменной окружения в переменную bot_token
print(bot_token)
