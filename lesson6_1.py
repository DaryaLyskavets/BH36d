#Написать функцию перевода десятичного числа в двоичное и обратно, без
#использования функции int
def num_bin(number):
    str_bin = ''
    while number > 0:
        str_bin = str(number % 2) + str_bin
        number //= 2
    print(str_bin)

num = int(input())
num_bin(num)
