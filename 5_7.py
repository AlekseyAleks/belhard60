# Дан список чисел, отсортировать его по возрастанию без использования sort и sorted

numbers_list = [3, 5, 4, 1, 2, 7, 6, 9, 8, 10]
sort_list = []
for i in numbers_list.copy():
    min_value = min(numbers_list)
    min_index = numbers_list.index(min_value)
    del numbers_list[min_index]
    sort_list.append(min_value)
print(sort_list)
