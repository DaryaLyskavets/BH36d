# Дан список рандомных чисел, необходимо отсортировать его в виде, сначала четные, потом нечётные
from random import randint

numbers = [randint(0, 100) for _ in range(randint(0, 10))]
print(numbers)


def sort_even_odd(number):
    even = []
    odd = []
    for i in number:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
    return even + odd

print(sort_even_odd(numbers))
