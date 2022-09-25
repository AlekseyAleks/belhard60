# Дан список рандомных чисел, необходимо отсортировать его в виде,
# сначала четные, потом нечётные

def sorting_even_odd(some_list: list) -> list:
    even_numbers = []
    odd_numbers = []
    for i in some_list:
        if i % 2:
            odd_numbers.append(i)
        else:
            even_numbers.append(i)
    return [even_numbers, odd_numbers]


sort_list = sorting_even_odd(some_list=[2, 5, 6, 2, 8, 7, 3, 1, 1, 9, 8])
print(f'Четные: {sort_list[0]}\nНечетные: {sort_list[1]}')
