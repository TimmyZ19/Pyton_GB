# Даны два файла, в каждом из которых находится запись многочленов. Задача - сформировать файл, содержащий сумму многочленов

import random


def polynom_sum(name_1: str, name_2: str):
    with open(name_1, "r", encoding="utf-8") as my_file_1, \
            open(name_2, "r", encoding="utf-8") as my_file_2:
        first = my_file_1.readlines()
        second = my_file_2.readlines()

        if len(first) == len(second):
            with open("summ_polynom.txt", "a", encoding="utf-8") as my_file_3:
                for i, v in enumerate(first):
                    my_file_3.write(f"{v[:-5]} + {second[i]}")
        else:
            print("Содержимое файлов не совпадает!")


polynom_sum("poly.txt", "poly_2.txt")
