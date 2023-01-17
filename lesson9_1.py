# 1. Написать класс Car
# Конструктор класса принимает атрибуты:
# color: str (цвет)
# count_passenger_seats: int (количество пассажирских мест)
# is_baby_seat: bool (наличие десткого кресла)
# is_busy: bool (определяется внутри конструктора со значением False, не принимается на
# вход)
# 1.1 Написать магический метод __str__ выводящий форматированную строку с информацией
# об автомобиле

class Car:

    @classmethod
    def __init__(cls, color: str, count_passenger_seats: int, is_baby_seat: bool, is_busy: bool):
        cls.is_busy = False
        cls.is_baby_seat = is_baby_seat
        if is_baby_seat:
            cls.is_baby_seat = 'With baby seat'
        else:
            cls.is_baby_seat = 'Without baby seat'
        cls.color = color
        cls.count_passenger_seats = count_passenger_seats
    @classmethod
    def __str__(cls):
        return f'Car: color = {cls.color}, passenger seats = {cls.count_passenger_seats}, ' \
               f'baby seat = {cls.is_baby_seat}'


print(Car('black', 4, True, is_busy=False))
