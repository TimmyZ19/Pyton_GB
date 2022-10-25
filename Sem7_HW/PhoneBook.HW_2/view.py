def User_selection():
    user_menu = ("Импорт справочника", "Экспорт справочника")
    for i in enumerate(user_menu, 1):
        print(i[0], i[1])
    while True:
        try:
            number = int(input("Введите № пункта: "))
            if 1 <= number <= 2:
                return number
            else:
                raise ValueError
        except ValueError:
            print("Введите число от 1 до 2: ")


def User_data_entry():
    name = input("Введите имя: ")
    surname = input("Введите фамилию: ")
    phone = input("Введите № телефона: ")
    comment = input("Введите описание: ")
    directory_entry = {
        "name": name,
        "surname": surname,
        "phone": phone,
        "comment": comment
    }
    return directory_entry
