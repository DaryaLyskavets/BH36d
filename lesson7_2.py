# На вход функции поступает список словарей humans и gender (m/w), каждый словарь
# содержит ключи: gender(пол), height(рост) людей, вернуть средний рост людей
# указанного пола

humans = [{'gender': 'm', 'height': '186'},
          {'gender': 'w', 'height': '165'},
          {'gender': 'm', 'height': '182'},
          {'gender': 'w', 'height': '168'},
          {'gender': 'w', 'height': '162'},
          {'gender': 'm', 'height': '181'}]


def average_height(humans, gender):
    total = 0
    all_height = []
    for i in humans:
        if i.get('gender') == gender:
            all_height.append(i.get('height'))
    for i in all_height:
        total += int(i)
    return total / len(all_height)


gender = input()
print(average_height(humans, gender))
