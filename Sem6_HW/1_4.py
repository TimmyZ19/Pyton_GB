# Функция принимает в качестве аргументов строки в формате «Имя Фамилия», возвращает словарь,
# ключи — первые буквы фамилий, значения — словари, реализованные по схеме предыдущего задания

def dictionary_people_lastname(people_list):
    result = {}
    for i in sorted(people_list):
        result.setdefault(i.split()[1][0], {}).setdefault(i.split()[0][0], []).append(i)
    return result


name_officers = ("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева", "Юнона Ветрякова",
                 "Борис Аркадьев", "Антон Серов", "Павел Анисимов")

print(dictionary_people_lastname(name_officers))
