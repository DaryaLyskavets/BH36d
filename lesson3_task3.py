name = input()
age = int(input())
city = input()

print(f'''Hello, my name is {name}. I am {age} years old. I live in {city}''')
print('Hello, my name is {}. I am {} years old. I live in {}'.format(name, age, city))
print("Hello, my name is %s. I am %d years old. I live in %s" %(name, age, city))