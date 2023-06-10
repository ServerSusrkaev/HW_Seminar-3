# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. В последующих
#  строках записаны N целых чисел Ai. Последняя строка содержит число X

import random

arrSize = int(input('Укажите размер массива: '))
array = []

for index in range(arrSize):
    array.append(random.randint(1, arrSize))

searchNumber = int(input('Укажите искомое значение: '))
count = 0

for item in array:
    if item == searchNumber:
        count += 1
print(f'Значение {searchNumber} встречается в массиве {count} раз(а)')
print(array)
