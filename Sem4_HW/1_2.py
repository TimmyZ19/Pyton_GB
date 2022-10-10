# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

def prime_factors(num):
    prime_list = []
    a = 2
    while num > 1:
        if num % a == 0:
            prime_list.append(a)
            num //= a
        else:
            a += 1
    return prime_list


print(prime_factors(int(input('Введите число N: '))))
