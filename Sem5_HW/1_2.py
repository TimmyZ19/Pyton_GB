# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.Входные и выходные данные хранятся в
# отдельных текстовых файлах

import itertools
import os


def rle_encode(text="input_data.txt", compress_text="output_data.txt"):
    if os.path.exists(text) and os.path.exists(compress_text):
        with open(text) as my_f_1, \
                open(compress_text, "a") as my_f_2:
            for i in my_f_1:
                my_f_2.write("".join([f"{len(list(v))}{ch}" for ch, v in itertools.groupby(i)]))
    else:
        print("Файлы отсутствуют в системе!")


def rle_decode(name):
    if os.path.exists(name):
        with open(name) as my_f:
            n = ""
            for k in my_f:
                w_nums = []
                for i in k.strip():
                    if i.isdigit():
                        n += i
                    else:
                        w_nums.append([int(n), i])
                        n = ""
                print("".join(itertools.starmap(lambda x, y: x * y, w_nums)))
    else:
        print("Файлы отсутствуют в системе!")


rle_encode(input("Введите имя файла с входными данными: "), input("Введите имя файла для записи: "))
rle_decode(input("Введите имя файла для декодирования: "))
