# Дан список чисел, необходимо его развернуть
my_list = [45, 1, 3, 5, 0, -1, 9, -3, 5]

def reverse_list(numbers):
    rev_numbers = []
    for i in range(len(numbers) - 1, -1, -1):
        rev_numbers.append(numbers[i])
    print(rev_numbers)


reverse_list(my_list)
