# Вводятся две строки, a и b, и возвращать количество раз,
# когда в обеих строках под одинаковыми индексами стоит одна и та же пара букв.

list1 = input('Введите первую строку: ')
list2 = input('Введите вторую строку: ')
if len(list1) > len(list2):
    length_string = len(list2)
else:
    length_string = len(list1)
for i in range(length_string):
    if list1[i] == list2[i]:
        print(f'Повторяется \"{list1[i]}\" с индексом \"{i}\"')
