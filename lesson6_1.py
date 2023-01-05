#Написать функцию перевода десятичного числа в двоичное и обратно, без
#использования функции int
def num_bin(number):
    str_bin = ''
    while number > 0:
        str_bin = str(number % 2) + str_bin
        number //= 2
    print(str_bin)
    number = 0
    len_bin = len(str_bin)
    for i in range(0, len_bin):
        number += int(str_bin[i]) * (2**(len_bin - i - 1))
    print(number)

num = int(input())
num_bin(num)
