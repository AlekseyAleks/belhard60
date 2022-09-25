# Дан список чисел и на вход поступает число N, необходимо сместить список на
# указанное число, пример: [1,2,3,4,5,6,7] N=3 ответ: [5,6,7,1,2,3,4]

def dislocation(some_list: list, number_shift: int) -> list:
    for i in range(number_shift.__abs__()):
        if number_shift > 0:
            number_remove = some_list.pop(len(some_list) - 1)
            some_list.insert(0, number_remove)
        else:
            number_remove = some_list.pop(0)
            some_list.append(number_remove)
    return some_list


print(dislocation(some_list=[1, 2, 3, 4, 5, 6, 7, 8, 9], number_shift=0))
