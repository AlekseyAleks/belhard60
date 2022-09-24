# Написать функцию перевода десятичного числа в двоичное и обратно,
# без использования функции int

import math


def conversion_to_binary(decimal: int) -> int:
    result = ''
    while decimal > 0:
        result = str(decimal % 2) + result
        decimal = decimal // 2
    return result


def conversion_to_decimal(binary: int) -> int:
    text = str(binary)
    decimal = 0
    for d in text:
        decimal = decimal * 2 + math.ceil(float(d))  # без использования функции int
    return decimal


print(conversion_to_binary(decimal=123))  # 1111011
print(conversion_to_decimal(binary=1111011))  # 123
