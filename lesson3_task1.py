text = input()
print(text.replace(' ', '-'))

words = text.split(' ')
text2 = '-'.join(words)
print(text2)