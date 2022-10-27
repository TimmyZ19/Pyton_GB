import csv
from prettytable import from_csv


def Import(file):
    contacts = open(file, 'r', encoding='utf-8')
    reader = list(csv.reader(contacts))
    try:
        lastID = str(int(reader[-1][0]) + 1)
    except IndexError:
        lastID = '1'
    contacts.close()
    contacts = open(file, 'a', encoding='utf-8')
    secondName = input('Фамилия: ')
    firstName = input('Имя: ')
    patronymic = input('Отчетство: ')
    classNum = input('Класс: ')
    classLiter = input('Литер класса: ')
    birthDate = input('Дата рождения: ')
    contacts.write(
        lastID + ',' + secondName + ',' + firstName + ',' + patronymic + ',' + classNum + ',' + classLiter + ',' + birthDate + '\n')
    contacts.close()
    print('Данные записаны')


def PrintDataBase(file):
    with open(file, 'r', encoding='utf-8') as fp:
        contacts = from_csv(fp)
    print(contacts)


def FindStudent(file):
    secondName = input('Фамилия => ')
    firstName = input('Имя => ')
    patronymic = input('Отчество => ')
    contacts = open(file, 'r', encoding='utf-8')
    reader = list(csv.reader(contacts))
    flag = False
    for i in range(1, len(reader)):
        if secondName in reader[i] and firstName in reader[i] and patronymic in reader[i]:
            print(' | '.join(reader[0]))
            print(' | '.join(reader[i]))
            flag = True
    if not flag:
        print('Ученики не найдены')
    contacts.close()


def PrintClass(file):
    contacts = open(file, 'r', encoding='utf-8')
    reader = list(csv.reader(contacts))
    classNum = input('Номер класса => ')
    classLiter = input('Литер класса => ')
    flag = False
    for i in range(1, len(reader)):
        if classNum in reader[i] and classLiter in reader[i]:
            if not flag:
                print(' | '.join(reader[0]))
            print(' | '.join(reader[i]))
            flag = True
    if not flag:
        print('Ученики не найдены')
    contacts.close()
