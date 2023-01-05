# Код Морзе для представления цифр и букв использует тире и точки. Напишите
# функцию для кодирования текстового сообщения в соответствии с кодом Морзе.
# (словари в помощь)
def morze(text):
    morze_dict = {'a': '•—', 'b': '—•••', 'c': '—•—•', 'd': '—••', 'e': '•', 'f': '••—•',
                  'g': '——•', 'h': '••••', 'i': '••', 'j': '•———', 'k': '—•—', 'l': '•—••',
                  'm': '——', 'n': '—•', 'o': '———', 'p': '•——•', 'q': '——•—', 'r': '•—•',
                  's': '•••', 't': '—', 'u': '••—', 'v': '•••—', 'w': '•——', 'x': '—••—',
                  'y': '—•——', 'z': '——••'
                  }
    a = [morze_dict.get(i) for i in text]
    return a

print(*morze(input()))
