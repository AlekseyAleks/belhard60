# Дан список чисел, необходимо для каждого элемента посчитать сумму его соседей,
# для крайних чисел одним из соседей является число с противоположной стороны списка

def sum(some_list: list) -> list:
    my_list = []
    for i in range(len(some_list)):
        if i == len(some_list) - 1:
            my_list.append(some_list[i - 1] + some_list[0])
        else:
            my_list.append(some_list[i + 1] + some_list[i - 1])
    return my_list


print(sum(some_list=[1, 2, 3, 4, 5]))
