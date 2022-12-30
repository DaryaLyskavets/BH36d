# Сделать калькулятор: у пользователя спрашивается число,
# потом действие и второе число
number = float(input())
action = input()
number_2 = float(input())

if action == '+':
    answer = number + number_2
elif action == '-':
    answer = number - number_2
elif action == '*':
    answer = number * number_2
elif action == '/' and number_2 != 0:
    answer = number / number_2
elif number_2 == 0:
    answer = 'На ноль делить нельзя!'
else:
    answer = 'Введите +, -, * или /'
print(answer)



