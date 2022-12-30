# **Вывести четные числа от 2 до N по 5 в строку

n = int(input())
even_num = []
for i in range(2, n + 1, 2):
    even_num.append(i)
for j in range(0, len(even_num), 5):
    print(even_num[j:j + 5])
