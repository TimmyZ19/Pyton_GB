#  Представлен список чисел. Необходимо вывести элементы исходного списка,
#  значения которых больше предыдущего элемента. Use comprehension.

import random

def values_greater_previous(num):
    m_list = random.sample(range(num ** 2), num)
    print(m_list)
    return [m_list[num] for num in range(1, len(m_list)) if m_list[num] > m_list[num - 1]]


print(values_greater_previous(int(input("Введите кол-во элементов списка: "))))