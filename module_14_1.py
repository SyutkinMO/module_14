# -----------------------Создание БД, добавление, выбор и удаление элементов.-----------------------

"""CRUD - Create, Read, Update, Delete"""

import sqlite3

"""Создайте таблицу Users, если она ещё не создана. В этой таблице должны присутствовать следующие поля:
id - целое число, первичный ключ
username - текст (не пустой)
email - текст (не пустой)
age - целое число
balance - целое число (не пустой)"""

connection = sqlite3.connect('not_telegram.db')  # подключение к базе данных
cursor = connection.cursor()  # создание курсора для навигации

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
''')  # команды пишутся большими буквами

# cursor.execute('INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)',
               #('', '', '', ''))  # стандартное заполнение БД

for i in range(10):
    cursor.execute('INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)',
                   (f'User{i + 1}', f'example{i + 1}@gmail.com', f'{(i + 1) * 10}',
                    '1000'))  # заполнение БД 10-ю записями
# Чтобы каждый раз не повторялось создание новых пользователей далее запись комментируется

"""Обновите balance у каждой 2ой записи начиная с 1ой на 500:"""
i = 1
while i < 10:
    cursor.execute('UPDATE Users SET balance = ? WHERE username = ?', (500, f'User{i}'))
    i += 2

"""Удалите каждую 3ую запись в таблице начиная с 1ой"""

i = 1
while i <= 10:
    cursor.execute('DELETE FROM Users WHERE username = ?',
                   (f'User{i}',))  # Важно оставить в конце запятую, так как должен передаваться кортеж
    i += 3

"""Сделайте выборку всех записей при помощи fetchall(), где возраст не равен 60 и выведите их в консоль в следующем 
формате (без id):
Имя: <username> | Почта: <email> | Возраст: <age> | Баланс: <balance>"""

cursor.execute('SELECT username, email, age, balance FROM Users WHERE age != ?', (60,))
users = cursor.fetchall()
for user in users:
    print(f'Имя: {user[0]} | Почта: {user[1]} | Возраст: {user[2]}, Баланс: {user[3]}')

connection.commit()
connection.close()  # закрыть соединение
