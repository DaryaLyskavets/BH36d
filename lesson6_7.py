# Дан список чисел, необходимо для каждого элемента посчитать сумму его
# соседей, для крайних чисел одним из соседей является число с противоположной стороны списка

def count_summ(num):
    a = []
    for i in range(0, len(num) - 1):
        a.append(num[i - 1] + num[i + 1])
    a.append(num[-2] + num[0])
    print(a)


numbers = [1, 2, 3, 4, 5]
count_summ(numbers)
