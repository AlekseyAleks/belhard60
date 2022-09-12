# Заполнить список степенями числа 2 (от 2^1 до 2^n).

entered_extent = int(input('Введите степень: '))
my_list = [2 ** (i + 1) for i in range(entered_extent)]
print(my_list)
