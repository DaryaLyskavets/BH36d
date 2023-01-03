# # # # # # # number = input()
# # # # # # # summa = 0
# # # # # # # for i in number:
# # # # # # #     summa += int(i)
# # # # # # # print(summa)
# # # # # #
# # # # # #
# # # # # # text = input('введи число' )
# # # # # # while not text.isdigit():
# # # # # #     text = input('введи число' )
# # # # # # print('finish')
# # # # #
# # # # # numbers = [1, 2, 2, 2, 5, 5, 8, 2, 5, 2, 6, 8, 2, 9]
# # # # # while 2 in numbers:
# # # # #     numbers.remove(2)
# # # # # print(numbers)
# # # #
# # # #
# # # # numbers = [1, 2, 2, 2, 5, 5, 8, 2, 5, 2, 6, 8, 2, 9]
# # # # for _ in range(numbers.count(2)):
# # # #     numbers.remove(2)
# # # #
# # #
# # # # num = int(input())
# # # # list = []
# # # # for i in range(num):
# # # #     if num >= 2**i:
# # # #         list.append(i)
# # # # print(max(list))
# # # n = int(input())
# # # i = 0
# # # while 2 ** i <= n:
# # #     i += 1
# # # i -= 1
# # # print(i)
# # #
#
# #
# # summa = int(input())
# # target = summa *2
# # percent = int(input())
# # year = 0
# # while summa < target:
# #     summa *= percent/100
# #     year+=1
# # print(year)
# . Реализовать бинанрный поиск по упорядоченному списку, суть бинарного поиска заключается в дроблении списка на половину
# 2. Реализовать генерацию списка списков рандомных чисел N размера (квадратная матрица)
#
# #поиск числа а в списке list
# from random import randint
#
# a = randint(1, 15)
# list_1=[]
# for i in range(1, 16):
#     list_1.append(i)
# print(a)
# low = 0
# high = len(list_1) - 1
# mid = (low + high) // 2
# while a != list_1[mid]:
#     if a == list_1[mid]:
#         print(mid)
#     elif a > list_1[mid]:
#         low = mid + 1
#     elif a < list_1[mid]:
#         high = mid - 1
#     mid = (low + high) // 2
# print(list_1[mid])
#
# from random import randint
# n = int(input())
# matrix = []
# for i in range(n):
#     row = []
#     for j in range(n):
#         number = randint(1, 11)
#         row.append(number)
#     matrix.append(row)
#
# for k in range(n):
#     print(matrix[k])
#
# for i in range(n):
#     for j in range(n):
#         matrix = [randint(0, 9)]
#         print(matrix, sep='\n', end = '\n')


# matrix = [[randint(0, 9) for _ in range(n)] for _ in range(n)]
# print(*matrix, sep = '\n', end = '\n')