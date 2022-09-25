# Дан словарь словарей, ключ внешнего словаря - id пользователя,
# значение - словарь с данными о пользователе (имя, фамилия, телефон, почта),
# вывести имена тех, у кого не указана почта (нет ключа email или значение этого ключа -
# пустая строка)

dict_data_base = {
    'id000111': {'name': 'Alex', 'surname': 'Borov', 'phone': '+375291212121', 'mail': 'ndnd@gmail.com'},
    'id000222': {'name': 'Jon', 'surname': 'Motir', 'phone': '+375298765443', '': 'cxvfd@gmail.com'},
    'id000333': {'name': 'Bob', 'surname': 'Corew', 'phone': '+375298765643', 'mail': ''},
    'id000444': {'name': 'Jin', 'surname': 'Miserti', 'phone': '+375296454533', '': ''},
    'id000555': {'name': 'Leon', 'surname': 'Aster', 'phone': '+375293534354', 'mail': 'lnhbs@gmail.com'},
}


def check_email():
    for i in dict_data_base.values():
        name = i['name']
        surname = i['surname']
        if '' in i.keys() and '' in i.values():
            print(f'У пользователя {name} {surname} отсутствуют \"Ключ и Значение email\"')
        elif '' in i.keys():
            print(f'У пользователя {name} {surname} отсутствует \"Ключ email\"')
        elif '' in i.values():
            print(f'У пользователя {name} {surname} отсутствует \"Значение email\"')


check_email()
