# Заполнить список степенями числа 2 (от 2^1 до 2^n).

entered_extent = int(input('Введите степень: '))
my_list = [None] * entered_extent  # [None, None, ..., None]
for i in range(len(my_list)):
    my_list[i] = 2 ** (i + 1)
print(my_list)
