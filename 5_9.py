# Вводится цисло, вывести таблицу умножения от 1 до 10 на это число

number = int(input('Введите число от 1 до 10: '))
for i in range(1, 11):
    print(f'{number} x {i} = {number * i}')
