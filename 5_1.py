# Вывести первые N чисел кратные M и больше K

first_numbers = int(input('Введите число выводимых первых чисел: '))
multiplicity = int(input('Введите кратность: '))
more_than = int(input('Больше какого значения: '))
result = []
counter = 1
while counter <= first_numbers:
    more_than += 1
    if not more_than % multiplicity:
        result.append(more_than)
        counter += 1
print(result)