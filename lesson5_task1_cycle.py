#Вводится число, найти его максимальную цифру
number = input()
elem = []
for i in number:
    elem.append(i)
print(max(elem))