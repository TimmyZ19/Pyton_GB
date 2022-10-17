# Напишите программу, удаляющую из текста все слова, содержащие "абв". В тексте используется разделитель пробел

import random


def list_random_words(count_words, values):
    if count_words < 0:
        print('Введите корректное кол-во')
    w_list = []
    for i in range(count_words):
        generation_w = random.sample(values, 3)
        w_list.append("".join(generation_w))
    return w_list


def filtr_remove_words(res_list):
    res_list = list(filter(lambda x: 'абв' not in x, res_list.split()))
    return " ".join(res_list)


count_words = int(input('Кол-во комбинаций в списке: '))
res_list = (" ".join(map(str, list_random_words(count_words, 'абв'))))

print(res_list)
print(filtr_remove_words(res_list))
