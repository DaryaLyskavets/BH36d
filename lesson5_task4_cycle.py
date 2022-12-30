# Количество монет
price = int(input())
print(price // 25 + price % 25 // 10 + price % 25 % 10 // 5 + price % 5)

counter = 0
while price >= 25:
    price = price - 25
    counter += 1
while 10 <= price < 25:
    price = price - 10
    counter += 1
while 5 <= price < 10:
    price = price - 5
    counter += 1
while 1 <= price < 5:
    price = price - 1
    counter += 1
print(counter)
