# На вход функции подается словарь: ключ - название команды, значение - количество
# очков, отсортировать и вернуть данный словарь по убыванию значений

teams = {'name_1': 3,
         'name_2': 0,
         'name_3': 5,
         'name_4': 2,
         'name_5': 1,
         'name_6': 9
         }


def get_sort_dict(my_dict: dict):
    my_dict = {i: my_dict[i] for i in sorted(my_dict, key=my_dict.get, reverse=True)}
    return my_dict


print(get_sort_dict(teams))
