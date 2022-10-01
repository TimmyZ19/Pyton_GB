#  Задайте список, состоящий из произвольных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётных позициях(не индексах).
# in
# 5
#
# out
# [10, 2, 3, 8, 9]
# 22
import random


def sum_random_num_list(count_num):
    if count_num > 0:
        arr = []
        for i in range(count_num):
            arr.append(random.randint(0, 10))
        print(arr)
        sum_el = 0
        for j in range(len(arr)):
            if j % 2 == 0:
                sum_el += arr[j]
        print(f'Сумма элементов нечетных позиций = {sum_el}')
    else:
        print("Error. count_num can't be < 0")


sum_random_num_list(int(input('Введите кол-во элементов списка: ')))
