# Реализуйте алгоритм перемешивания списка. НЕ ИСПОЛЬЗОВАТЬ ВСТРОЕННЫЕ БИБЛИОТЕКИ SHUFFLE, 
# максимум использование библиотеки Random для получения случайного int

import random

list = []
quantity = int(input('Введите количество элементов списка: '))
i = 1
while i <= quantity:
    list.append(random.randint(1,10))
    i+=1
print(f'Исходный список: {list}')

x = 0
for j in list:
    temp = random.randint(1,quantity-1)
    temp_num = list[temp]
    list[temp] = j
    list[x] = temp_num
    x+=1
    
print(f'Результирующий список: {list}')

