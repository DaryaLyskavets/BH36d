#Вывести первые N цисел кратные M и больше K
n = int(input())
m = int(input())
k = int(input())
i = 0
count = 0
while count < n:
    i += 1
    if i % m == 0 and i > k:
        count += 1
        print(i, end=' ')