#поиск числа а в списке list (бинарный поиск)
from random import randint

a = randint(1, 15)
list_1=[]
for i in range(1, 16):
    list_1.append(i)
print(a)
low = 0
high = len(list_1) - 1
mid = (low + high) // 2
while a != list_1[mid]:
    if a == list_1[mid]:
        print(mid)
    elif a > list_1[mid]:
        low = mid + 1
    elif a < list_1[mid]:
        high = mid - 1
    mid = (low + high) // 2
print(list_1[mid])
