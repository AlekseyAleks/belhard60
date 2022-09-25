# Дан список чисел, необходимо его развернуть без использования метода revese и
# функции reversed, а так же дополнительного списка и среза

def reverse_list(some_list: list) -> list:
    counter = 0
    for i in range(len(some_list) - 1):
        number_remove = some_list.pop(len(some_list) - 1)
        some_list.insert(counter, number_remove)
        counter += 1
    return some_list


print(reverse_list(some_list=[1, 2, 3, 4, 5, 6, 7, 8, 9]))  # [9, 8, 7, 6, 5, 4, 3, 2, 1]
