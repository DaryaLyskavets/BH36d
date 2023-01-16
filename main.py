# # # # # # # # number = input()
# # # # # # # # summa = 0
# # # # # # # # for i in number:
# # # # # # # #     summa += int(i)
# # # # # # # # print(summa)
# # # # # # #
# # # # # # #
# # # # # # # text = input('введи число' )
# # # # # # # while not text.isdigit():
# # # # # # #     text = input('введи число' )
# # # # # # # print('finish')
# # # # # #
# # # # # # numbers = [1, 2, 2, 2, 5, 5, 8, 2, 5, 2, 6, 8, 2, 9]
# # # # # # while 2 in numbers:
# # # # # #     numbers.remove(2)
# # # # # # print(numbers)
# # # # #
# # # # #
# # # # # numbers = [1, 2, 2, 2, 5, 5, 8, 2, 5, 2, 6, 8, 2, 9]
# # # # # for _ in range(numbers.count(2)):
# # # # #     numbers.remove(2)
# # # # #
# # # #
# # # # # num = int(input())
# # # # # list = []
# # # # # for i in range(num):
# # # # #     if num >= 2**i:
# # # # #         list.append(i)
# # # # # print(max(list))
# # # # n = int(input())
# # # # i = 0
# # # # while 2 ** i <= n:
# # # #     i += 1
# # # # i -= 1
# # # # print(i)
# # # #
# #
# # #
# # # summa = int(input())
# # # target = summa *2
# # # percent = int(input())
# # # year = 0
# # # while summa < target:
# # #     summa *= percent/100
# # #     year+=1
# # # print(year)
# # . Реализовать бинанрный поиск по упорядоченному списку, суть бинарного поиска заключается в дроблении списка на половину
# # 2. Реализовать генерацию списка списков рандомных чисел N размера (квадратная матрица)
# #
# # #поиск числа а в списке list
# # from random import randint
# #
# # a = randint(1, 15)
# # list_1=[]
# # for i in range(1, 16):
# #     list_1.append(i)
# # print(a)
# # low = 0
# # high = len(list_1) - 1
# # mid = (low + high) // 2
# # while a != list_1[mid]:
# #     if a == list_1[mid]:
# #         print(mid)
# #     elif a > list_1[mid]:
# #         low = mid + 1
# #     elif a < list_1[mid]:
# #         high = mid - 1
# #     mid = (low + high) // 2
# # print(list_1[mid])
# #
# # from random import randint
# # n = int(input())
# # matrix = []
# # for i in range(n):
# #     row = []
# #     for j in range(n):
# #         number = randint(1, 11)
# #         row.append(number)
# #     matrix.append(row)
# #
# # for k in range(n):
# #     print(matrix[k])
# #
# # for i in range(n):
# #     for j in range(n):
# #         matrix = [randint(0, 9)]
# #         print(matrix, sep='\n', end = '\n')
#
#
# # matrix = [[randint(0, 9) for _ in range(n)] for _ in range(n)]
# # print(*matrix, sep = '\n', end = '\n')
#
# from random import *
# print('Привет Мир, я магический шар, и я знаю ответ на любой твой вопрос.')
# name = input('Привет, напиши свое имя:' )
# print('Привет', name)
# answers = ["Бесспорно", "Предрешено", "Никаких сомнений", "Определённо да",
#            "Можешь быть уверен в этом", "Мне кажется - да", "Вероятнее всего",
#            "Хорошие перспективы", "Знаки говорят - да", "Да", "Пока неясно, попробуй снова",
#            "Спроси позже", "Лучше не рассказывать", "Сейчас нельзя предсказать",
#            "Сконцентрируйся и спроси опять", "Даже не думай", "Мой ответ - нет",
#            "По моим данным - нет", "Перспективы не очень хорошие", "Весьма сомнительно"]
# while True:
#     input('Задавай вопрос:' )
#     print(choice(answers))
#     print('Хочешь задать еще вопрос?')
#     answ = input()
#     if answ == 'нет' or answ == 'no':
#         print('Возвращайся если возникнут вопросы!')
#         break
#     elif answ == 'yes' or answ == 'да':
#         continue

# def find_all(target, symbol):
#     a =[]
#     for i in range(len(target)):
#         if target[i] == symbol:
#             a.append(i)
#     return a
#
# tar = input()
# sym = input()
#
# print(find_all(tar, sym))

# class Student:
#     def __init__(self, first_name: str, group: int, marks: list[int]):
#         self.first_name = first_name
#         self.group = group
#         self.marks = marks
#     def __str__(self) -> str:
#         return f'Student: {self.first_name=} {self.group} {self.marks}'
#     @staticmethod
#     def student_sort(student: list['Student']) -> list['Student']:
#
#         return student

class Category:
    categories = []

    @classmethod
    def add(cls, name: str):
        for i in cls.categories:
            if name not in cls.categories:
                cls.categories.append(name)
                return cls.categories.index(name)
            else:
                raise ValueError

    @classmethod
    def get(cls, index: int):
        return cls.categories[index]

    @classmethod
    def delete(cls, index: int) -> None:
        # if index in range(len(cls.categories():
        #     del cls.categories[index]
        try:
            del cls.categories[index]
        except IndexError:
            pass

    @classmethod
    def update(cls,index: int, new_name: str):
        if index not in range(len(cls.categories())):
            cls.add(new_name)
        elif new_name not in cls.categories:
            cls.categories[index] = new_name
        else:
            raise ValueError
