# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Без использования встроенной функции преобразования, без строк.
# in
# 88
# out
# 1011000

def convert_binary_num(num):
    m_list = []
    while num > 0:
        num_convert = (num % 2)
        m_list.append(num_convert)
        num //= 2
    m_list.reverse()
    return m_list


num = int(input('Введите число: '))
string_num = "".join(map(str, convert_binary_num(num)))
print(f"Число {num} в двоичной системе: {string_num}")
