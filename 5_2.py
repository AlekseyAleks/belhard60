# Сделать калькулятор: у пользователя спрашивается число,
# потом действие и второе число

first_number = int(input('Введите первое число: '))
operation = input('Укажите действие (+, -, *, /): ')
second_number = int(input('Введите второе число: '))
match operation:  # for Python 3.10 and more
    case '+':
        print(f'{first_number} + {second_number} = {first_number + second_number}')
    case '-':
        print(f'{first_number} - {second_number} = {first_number - second_number}')
    case '*':
        print(f'{first_number} * {second_number} = {first_number * second_number}')
    case '/':
        print(f'{first_number} / {second_number} = {first_number / second_number}')
    case _:
        print('Не верно указано действие!')
