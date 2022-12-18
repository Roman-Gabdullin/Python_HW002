# Реализуйте алгоритм перемешивания списка. НЕ ИСПОЛЬЗОВАТЬ ВСТРОЕННЫЕ БИБЛИОТЕКИ SHUFFLE, 
# максимум использование библиотеки Random для получения случайного int

import random

my_list = []
quantity = int(input('Введите количество элементов списка: '))
i = 1
while i <= quantity:
    my_list.append(random.randint(1,10))
    i+=1
print(f'Исходный список: {my_list}')

x = 0
for j in my_list:
    temp = random.randint(1,quantity-1)
    temp_num = my_list[temp]
    my_list[temp] = j
    my_list[x] = temp_num
    x+=1
    
print(f'Результирующий список: {my_list}')

