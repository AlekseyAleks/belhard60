# Без использования collections, написать программу, которая будет
# создавать словарь для подсчитывания количества вхождений каждой
# буквы в текст введенный с клавиатуры

text = input('Enter text: \n')
text = text.replace(',', '')
text = text.replace('.', '')
text = text.replace(' ', '')
my_dict = {}
for i in range(len(text)):
    my_dict[i] = text[i]
print(f'Колличество вхождений каждой буквы в текст: {list(my_dict)[-1]}')