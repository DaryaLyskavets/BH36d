# Дан словарь словарей, ключ внешнего словаря - id пользователя, значение -
# словарь с данными о пользователе (имя, фамилия, телефон, почта), вывести
# имена тех, у кого не указана почта (нет ключа email или значение этого ключа -
# пустая строка)

users = {1: {'name': 'pavel', 'surname': 'ivanov', 'phone': '2220', 'email': 'ivanov@gmail'},
         2: {'name': 'oleg', 'surname': 'petrov', 'phone': '2289'},
         3: {'name': 'lev', 'surname': 'popov', 'phone': '8220', 'email': ''},
         4: {'name': 'dima', 'surname': 'sidorov', 'phone': '20', 'email': 'sidorov@gmail'}
         }

for key, value in users.items():
    if not value.get('email'):
        print(key)
