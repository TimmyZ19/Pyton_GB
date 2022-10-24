from fractions import Fraction


def irrattional_operation(a: str, b: str, operator):
    f_a = Fraction(a)
    f_b = Fraction(b)
    return f_a+f_b if operator == '+' else f_a-f_b if operator == '-' \
        else f_a*f_b if operator == '*' else f_a/f_b if operator == '/' else False

