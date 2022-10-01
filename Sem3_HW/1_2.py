# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# in
# 4
#
# out
# [2, 5, 8, 10]
# [20, 40]

import random


def mult_random_num_list(count_num):
    if count_num > 0:
        arr = []
        for i in range(count_num):
            arr.append(random.randint(0, 10))
        print(arr)
        mult_arr = []
        while len(arr) > 1:
            mult_arr.append(arr[0] * arr[-1])
            del arr[0]
            del arr[-1]
        if len(arr) == 1:
            mult_arr.append(arr[0])
        print(f'Произведение пар списка = {mult_arr}')
    else:
        print("Error. count_num can't be < 0")


mult_random_num_list(int(input('Введите кол-во элементов списка: ')))
