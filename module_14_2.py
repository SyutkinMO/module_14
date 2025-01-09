# -----------------------Выбор элементов и функции в SQL запросах-----------------------

"""CRUD - Create, Read, Update, Delete"""

import sqlite3

connection = sqlite3.connect('not_telegram.db')  # подключение к базе данных
cursor = connection.cursor()  # создание курсора для навигации

# Удалите из базы данных not_telegram.db запись с id = 6
cursor.execute('DELETE FROM Users WHERE id = ?', (6,))

# Подсчитать общее количество записей.
cursor.execute('SELECT COUNT (*) FROM Users')
total_people = cursor.fetchone()[0]
print(total_people)

# Посчитать сумму всех балансов.
cursor.execute('SELECT SUM (balance) FROM Users')
total_balance = cursor.fetchone()[0]
print(total_balance)

# Вывести в консоль средний баланс всех пользователей.
print(total_balance / total_people)

connection.commit()
connection.close()  # закрыть соединение
