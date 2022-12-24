text = input()
text = text.replace(' ', '')
text = text.lower()
print(text == text[::-1])
