"""
Задание 2.

Пользователь вводит время в секундах.
Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
Используйте форматирование строк.

Пример:
Введите время в секундах: 3600
Время в формате ч:м:с - 1.0 : 60.0 : 3600
"""

time_sec = int(input("Введите время в секундах: "))
hour = time_sec / 3600
minute = time_sec / 60
sec = time_sec
print(f"time in format hh:mm:ss : {hour} : , {minute} : , {sec}")
