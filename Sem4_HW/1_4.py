# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (от 0 до 10) многочлена,
# записать в файл полученный многочлен не менее 3-х раз.

import random


def random_list_polynomial(num):
    if num < 1:
        return 0
    polynom = ""
    m_list = range(0, 10)
    with open("polynomial.txt", "a", encoding="utf-8") as my_file:
        for i in range(num, 0, -1):
            value = random.choice(m_list)
            if value:
                polynom += f"{value}*x^{i} {random.choice('+-')} "

        my_file.write(f"{polynom}{random.choice(m_list)} = 0\n")


for _ in range(3):
    random_list_polynomial(int(input('Задайте натуральную степень: ')))
