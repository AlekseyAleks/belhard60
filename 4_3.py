# *Заполнить словарь где ключами будут выступать числа от 0 до n, а
# значениями вложенный словарь с ключами "name" и "email", а значения
# для этих ключей будут браться с клавиатуры

keys = int(input(f'Enter the number of keys: '))
my_dict = {}
for i in range(keys):
    print(f'Key {i}')
    my_dict[i] = {'name': input('Enter name: '), 'email': input('Enter email: ')}
print(my_dict)
