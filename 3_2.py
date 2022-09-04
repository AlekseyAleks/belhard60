# Пользователь вводит 3 числа, найти среднее арифмитическое точность 3

print('Enter 3 numbers.')
first_number = float(input('1 number: '))
second_number = float(input('2 number: '))
third_number = float(input('3 number: '))
arithmetic_average = round((first_number + second_number + third_number) / 3, 3)
print(f'Arithmetic average: {arithmetic_average}')
