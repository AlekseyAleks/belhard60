# Дан список содержащий в себе различные типы данных, отфильтровать таким образом,
# чтобы остались только строки, использование дополнительного списка незаконно


def only_string(some_list: list) -> list:
    for i in some_list.copy():
        if not isinstance(i, str):
            some_list.remove(i)
    return some_list


print(only_string(some_list=[1, 'fffff', [1, 2], 'qqqq']))  # ['fffff', 'qqqq']
