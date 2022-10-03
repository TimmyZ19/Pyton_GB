# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов

def num_febonachi(num):
    arr = [0]
    j = 1
    for i in range(1, num + 1):
        if i % 2 == 0:
            arr.insert(0, -j)
        else:
            arr.insert(0, j)
        arr.append(j)
        j += arr[-2]
    return arr


num = int(input('Введите число: '))
print(f'Список чисел Фиббоначи: {num_febonachi(num)}')
