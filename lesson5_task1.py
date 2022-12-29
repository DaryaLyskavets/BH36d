#Вывести первые N цисел кратные M и больше K
n = int(input())
m = int(input())
k = int(input())
for i in range(n+1):
    if i % m == 0 and i > k:
        print(i, end=' ')