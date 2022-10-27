from functions import *


def Menu(path):
    print('База данных учеников')
    print('1 - внести нового ученика в базу')
    print('2 - вывести на экран всех учеников')
    print('3 - найти ученика по ФИО')
    print('4 - вывести на экран всех учеников определенного класса')
    print('0 - завершить работу')
    answer = int(input('Что вы хотите сделать: '))
    while answer != 0:
        if answer == 1:
            Import(path)
            break
        if answer == 2:
            PrintDataBase(path)
            break
        if answer == 3:
            FindStudent(path)
            break
        if answer == 4:
            PrintClass(path)
            break
    print('Работа завершена!')
