# Написать программу генерации треугольника паскаля указанной глубины

depth = int(input('Введите значение глубины треугольника Паскаля: '))
result = {}
inserted_list = []
for i in range(0, depth):
    for j in range(0, i + 1):
        if j == 0 or j == i:
            inserted_list.append(1)
        else: inserted_list.append(result[i - 1][j - 1] + result[i - 1][j])
    result[i] = inserted_list.copy()
    inserted_list.clear()
for k, v in result.items():
    print(k, '  ' * (depth - k), v)
