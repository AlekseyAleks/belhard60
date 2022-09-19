# Вводится строка, вывести из строки только цифры

text = input('Введите текст: ')
my_list = []
for i in range(len(text)):
    if text[i].isdigit():
        my_list.append(int(text[i]))
print(my_list)
