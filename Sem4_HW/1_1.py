# Вычислить число c заданной точностью d
# in
# Enter a real number: 9
# Enter the required accuracy '0.0001': 0.000001
# out
# 9.000000

import decimal


def numbser_accuracy(real_num, accuracy):
    num = decimal.Decimal(f"{real_num}")
    return num.quantize(decimal.Decimal(f"{accuracy}"))


real_num = float(input("Введите число: "))
accuracy = float(input("Введите точность округления в формате 0.0001: "))

print(numbser_accuracy(real_num, accuracy))
