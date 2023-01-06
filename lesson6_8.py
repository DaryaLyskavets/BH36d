# Дан словарь, ключ - Название страны, значение - список городов, на вход
# поступает город, необходимо сказать из какой он страны
country_city = {
    'Germany': 'Berlin',
    'Italy': 'Rome',
    'Spain': 'Madrid',
    'France': 'Paris',
    'Poland': 'Warsaw',
    'Belarus': 'Minsk',
    'Latvia': 'Riga'
}


def get_country(dictionary, my_city):
    for key, value in dictionary.items():
        if value.lower() == my_city.lower():
            return key


city = input('Enter the city:')
print(get_country(country_city, city))
