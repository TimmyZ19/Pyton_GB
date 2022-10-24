def number_input(num):
    a = 'первое' if not num else 'второе'
    return input(f'Введите {a} число: ')


def operator_input():
    return input('Введите необходимое действие: ')


def type_input():
    print('Выберите, с какими числами работать:')
    user_type = input(f'1 - рациональные\n2 - комплексные\n ')
    return 1 if user_type == '1' else 2 if user_type == '2' else 0