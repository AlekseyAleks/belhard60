# Пользователь вводит 3 числа, сказать сколько из них положительных и сколько отрицательных

print('Enter 3 numbers.')
count_negative = input('1 number: ').startswith('-') +\
                 input('2 number: ').startswith('-') +\
                 input('3 number: ').startswith('-')
print(f'Positive numbers: {3 - count_negative} \nNegative numbers: {count_negative}')
