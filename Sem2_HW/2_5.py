# Реализуйте алгоритм перемешивания списка. Без функции shuffle из модуля random.
# 10
# -> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# -> [0, 7, 6, 3, 4, 2, 9, 5, 1, 8]
import random

n = int(input('Введите число N:'))
m= []

for i in range(n):
    m.append(i)
print(m)

for i in range(len(m)):
    j = random.randint(0, len(m) - 1)
    temp = m[i]
    m[i] = m[j]
    m[j] = temp
print(m)