from dataclasses import dataclass


@dataclass()
class User:
    user_id: int
    name: str
    age: int
    email: str


user_1: User = User(42, 'Vasiliy', 23, 'vasya_pupkin@pochta.ru')
user_2: User = User(44, 'Vasiliy', 44, 'vasya_pupkin@ya.ru')
print(user_1)
print(user_2)

# Real example
@dataclass
class DatabaseConfig:
    db_host: str       # URL-адрес базы данных
    db_user: str       # Username пользователя базы данных
    db_password: str   # Пароль к базе данных
    database: str      # Название базы данных


@dataclass
class TgBot:
    token: str             # Токен для доступа к телеграм-боту
    admin_ids: list[int]   # Список id администраторов бота


@dataclass
class Config:
    tg_bot: TgBot
    db: DatabaseConfig
