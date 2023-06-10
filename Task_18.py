# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. В последующих  
# строках записаны N целых чисел Ai. Последняя строка содержит число X

import random

arrSize = int(input('Укажите размер массива: '))
array = []
index = 1

for index in range(1, arrSize + 1):
    array.append(index)

searchNumber = int(input('Укажите искомое значение: '))
number = 0
for item in range(len(array)):
    if array[item] == searchNumber:
        number = array[item - 1]

print(f'Самый близкий по величине элемент массива к искомому значению: {number}')