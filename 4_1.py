# Заполнить список степенями числа 2 (от 2^1 до 2^n).

extent = int(input('Введите степень: '))
none_list = [None] * extent  # [None, None, ..., None]
my_list = [2 for elm in none_list]
for i in range(len(my_list)):
    my_list[i] **= i + 1
print(my_list)
