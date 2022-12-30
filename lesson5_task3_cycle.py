# Угадай число
from random import randint

a = randint(1, 100)
num = input('Угадайте число от 1 до 100: ')
count = 1
while int(num) != a:
    if int(num) < 1 or int(num) > 100:
        print('Введите целое число в диапазоне от 1 до 100!')
    num = input('Попробуйте еще раз. Введите число от 1 до 100: ')
    count += 1
print('Ура! Вы угадали с', count, 'попытки')
