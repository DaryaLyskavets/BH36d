from csv import DictReader, reader, writer, DictWriter

with open(r'C:\Users\Admin\Desktop\table.csv', mode='a', encoding='utf-8') as file:

    w = DictWriter(file, fieldnames=('name', 'age', 'city'), delimiter=';')
    w.writerow({'name' : 'misha', 'age': '65', 'city': 'minsk'})

with open(r'C:\Users\Admin\Desktop\table.csv', mode='r', encoding='utf-8') as file:
    r = DictReader(file, delimiter=';')
    for user in r:
        print(user)





