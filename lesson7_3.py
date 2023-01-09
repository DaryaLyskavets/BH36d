# На вход функции поступает список словарей users, каждый словарь содержит ключи:
# id, name, referrer_id, id у каждого пользователя уникальный, referrer_id содержит id
# пользователя, кто пригласил данного пользователя и может быть пустым, посчитать
# для каждого пользователя, каждому пользователю добавить ключ referrals_count с
# количеством человек, которых он пригласил

users = [{'id': 11, 'name': 'Alex', 'referrer_id': '' },
         {'id': 22, 'name': 'Peter', 'referrer_id': 11 },
         {'id': 121, 'name': 'Ron', 'referrer_id': 33 },
         {'id': 33, 'name': 'Tom', 'referrer_id': 22},
         {'id': 144, 'name': 'Bob', 'referrer_id': 11 }
         ]

def get_referrals_count(users: dict):
