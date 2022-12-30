# **Вывести четные числа от 2 до N по 5 в строку

n = int(input())
count = 0
line = ''
for i in range(2, n + 1, 2):
    count += 1
    if count % 5 != 0:
        line += str(i) + ' '
    elif count % 5 == 0:
        line += str(i) + ' ' + '\n'
print(line)

# n = int(input())
# even_num = []
# for i in range(2, n + 1, 2):
#     even_num.append(i)
# for j in range(0, len(even_num), 5):
#     print(even_num[j:j + 5])