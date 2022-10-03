# Задайте список из произвольных вещественных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов

import random


def random_float_list(count_num):
    if count_num > 0:
        my_list = []
        for k in range(count_num):
            my_list.append(round(random.uniform(0, 10), 2))
        return my_list
    else:
        print("Error. count_num can't be < 0")


my_list = random_float_list(int(input("Введите кол-во элементов списка: ")))
print(my_list)


def difference_float(list):
    result = []
    for i in range(len(list)):
        result.append(round(list[i] - int(list[i]), 2))
    return result


t = difference_float(my_list)

print(f"Максимальное значение дробной части {max(t)}\n"
      f"Минимальное значение дробной части {min(t)}")
print(f"Разница между максимальным  и минимальным значением дробной части элементов = {round(max(t) - min(t), 2)}")
