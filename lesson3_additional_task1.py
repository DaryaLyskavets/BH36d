number = input()
first_num = number[:number.find('/')]
last_num = number[number.rfind('/') + 1:]
print(float(first_num) / float(last_num))
