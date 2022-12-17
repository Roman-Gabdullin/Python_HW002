# 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0,56 -> 11

import random


num = round(random.uniform(1,10), 3)
print(num)

while num != int(num):
    num *= 10

sum = 0

while num > 0:
    sum += num % 10
    num //= 10
print(f'Сумма цифр числа = {int(sum)}')



  