# Без использования collections, написать программу, которая будет
# создавать словарь для подсчитывания количества вхождений каждой
# буквы в текст введенный с клавиатуры

text = input('Enter text: \n')
text = text.replace(',', '')
text = text.replace('.', '')
text = text.replace(' ', '')
my_dict = {i: text.count(i) for i in text}
print(f'Количество вхождений каждой буквы в текст: {my_dict}')

