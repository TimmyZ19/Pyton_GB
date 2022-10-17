# Написать функцию, аргументы имена сотрудников, возвращает словарь, ключи — первые буквы имён, значения — списки,
# содержащие имена, начинающиеся с соответствующей буквы.

def dictionary_people_name(people_list):
    result = {}
    for i in sorted(people_list):
        key = i[0]
        if key not in result:
            result[key] = [i]
        result[key] += [i]
    return result


name_officers = ("Иван", "Мария", "Петр", "Илья", "Марина", "Петр", "Алина", "Бибочка")

print(dictionary_people_name(name_officers))