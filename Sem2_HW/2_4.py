# 4. Напишите программу, которая принимает на вход 2 числа. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях(не индексах).
# Position one: 1
# Position two: 3
# Number of elements: 5
# -> [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
# -> 15

position_one = int(input('Укажите позицию первого элемента: '))
position_two = int(input('Укажите позицию второго элемента: '))
n = int(input('Введите число N:'))
m = []

for i in range(-n,n+1):
    m.append(i)
print(f'Список: {m}')

if position_one > len(m) or position_two > len(m):
    print('Позиция за границей списка')
else:
    print(f'Произведение элементов {m[position_one-1]} и {m[position_two-1]}:  {m[position_one-1]*m[position_two-1]}')
