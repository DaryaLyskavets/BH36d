# Сделать калькулятор: у пользователя спрашивается число,
# потом действие и второе число
number = int(input())
action = input()
number_2 = int(input())

if action == '+':
    print(number + number_2)
elif action == '-':
    print(number - number_2)
elif action == '*':
    print(number * number_2)
elif action == '/':
    print(number / number_2)
else:
    print('Введите +, -, * или /')

try:
    number_2 = 0
except ZeroDivisionError:
    print('На ноль делить нельзя')

