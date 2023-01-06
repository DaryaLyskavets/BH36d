# Дан список содержащий в себе различные типы данных, отфильтровать таким
# образом, чтобы остались только строки
my_list = ['hello', 3, '45', 'python', 356, ['l', 'm'], '!']

print(*list(filter(lambda x: isinstance(x, str), my_list)))

def only_string(list):
    new_list = []
    for i in list:
        if isinstance(i, str):
            new_list.append(i)
    return new_list

print(*only_string(my_list))
