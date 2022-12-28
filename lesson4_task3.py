n = int(input('Введите число:', ))
dictionary = {i:
                  {'name': input('Введите имя:', ),
                   'email': input('Введите email:', )
                   }
              for i in range(n + 1)}
print(dictionary)
