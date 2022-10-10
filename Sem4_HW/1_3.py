# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной
# последовательности в том же порядке.

import random


def random_nums_list(count: int):
    if count < 0:
        print("Отрицательное кол-во чисел!")
        return []
    list_num = []
    for i in range(count):
        list_num.append(random.randrange(count))
    return list_num


def unique_elements_original(list_num: list):
    result = []
    m_list = {}.fromkeys(list_num, 0)
    for i in list_num:
        m_list[i] += 1
    for j in m_list:
        if m_list[j] == 1:
            result.append(j)
    return result


list_a = random_nums_list(int(input("Введите кол-во чисел: ")))
print(list_a)
print(unique_elements_original(list_a))
