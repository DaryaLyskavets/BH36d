# # # # # # number = input()
# # # # # # summa = 0
# # # # # # for i in number:
# # # # # #     summa += int(i)
# # # # # # print(summa)
# # # # #
# # # # #
# # # # # text = input('введи число' )
# # # # # while not text.isdigit():
# # # # #     text = input('введи число' )
# # # # # print('finish')
# # # #
# # # # numbers = [1, 2, 2, 2, 5, 5, 8, 2, 5, 2, 6, 8, 2, 9]
# # # # while 2 in numbers:
# # # #     numbers.remove(2)
# # # # print(numbers)
# # #
# # #
# # # numbers = [1, 2, 2, 2, 5, 5, 8, 2, 5, 2, 6, 8, 2, 9]
# # # for _ in range(numbers.count(2)):
# # #     numbers.remove(2)
# # #
# #
# # # num = int(input())
# # # list = []
# # # for i in range(num):
# # #     if num >= 2**i:
# # #         list.append(i)
# # # print(max(list))
# # n = int(input())
# # i = 0
# # while 2 ** i <= n:
# #     i += 1
# # i -= 1
# # print(i)
# #
#
# summa = int(input())
# target = summa *2
# percent = int(input())
# year = 0
# while summa < target:
#     summa *= percent/100
#     year+=1
# print(year)
