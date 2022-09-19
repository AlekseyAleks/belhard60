# Вводится число, посчитать факториал этого числа

factorial = int(input('Введите факториал: '))
result = 1
text = f'{factorial}! ='
for i in range(1, factorial + 1):
    result *= i
    if i == factorial:
        text += f' {i}'
    else:
        text += f' {i} *'
print(f'{text} = {result}')
