# **Вывести четные числа от 2 до N по 5 в строку

number_range = int(input('Введите значение до которого проверять на четность: '))
result = []
counter = 2
while counter <= number_range:
    if not counter % 2:
        result.append(counter)
        if len(result) == 5:
            print(result)
            result.clear()
    counter += 1
if len(result) >= 1:
    print('Не заполненный результат: ', result)
