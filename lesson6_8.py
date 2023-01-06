# Дан словарь, ключ - Название страны, значение - список городов, на вход
# поступает город, необходимо сказать из какой он страны

country = ('Germany', 'Italy', 'Spain', 'France', 'Poland', 'Belarus', 'Latvia')
city = ('Berlin', 'Rome', 'Madrid', 'Paris', 'Warsaw', 'Minsk', 'Riga')
country_city = dict(zip(country, city))


def get_country(dictionary, my_city):
    for key, value in dictionary.items():
        if value.lower() == my_city.lower():
            return key


city = input('Enter the city:')
print(get_country(country_city, city))
