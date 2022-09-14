# Пользователь вводит Имя, Возраст и Город,
# сформировать приветственное сообщение путем форматирования 3-мя способами

name = input('Enter name: ')
age = int(input('Enter age: '))
city = input('Enter city: ')
print('First solution:', 'Hello %s! You are %d years old. You are from the city of %s.' % (name, age, city))
print('Second solution:', 'Hello {}! You are {} years old. You are from the city of {}.'.format(name, age, city))
print('Third solution:', f'Hello {name}!', f'You are {age} years old.', f'You are from the city of {city}.')
