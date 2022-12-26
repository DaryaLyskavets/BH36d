keys = ('name', 'age', 'city')
value = ('alex', 43, 'minsk')
user = {keys[i] : value[i] for i in range(len(keys))}
print(user)