from random import randint

n = int(input())
matrix = []
for i in range(n):
    row = []
    for j in range(n):
        number = randint(1, 11)
        row.append(number)
    matrix.append(row)

for k in range(n):
    print(matrix[k])