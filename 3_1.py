# Пользователь вводит предложение, заменить все пробелы на "-" 2-мя способами

text = input("Enter text:\n")

print('First solution: ', text.replace(" ", "-"))

words = text.split(' ')

print(f'Second solution:', '-'.join(words))
