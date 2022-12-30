# Подсчитать среднее арифметическое N чисел, вводимых с клавиатуры
n = int(input())
summa = 0
for i in range(n):
    number = int(input())
    summa += number
print(summa / n)
