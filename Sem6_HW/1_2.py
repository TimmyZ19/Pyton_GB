# Для чисел в пределах от 20 до N найти числа, кратные 20 или 21. Use comprehension

def list_number(num):
    return [n for n in range(20, num + 1) if n % 20 == 0 or n % 21 == 0]


print(list_number(int(input("Введите число: "))))
