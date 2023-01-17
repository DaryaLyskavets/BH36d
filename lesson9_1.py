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

    def __init__(self, color: str, count_passenger_seats: int, is_baby_seat: bool, is_busy: bool):
        self.is_busy = False
        self.is_baby_seat = is_baby_seat
        if is_baby_seat:
            self.is_baby_seat = 'With baby seat'
        else:
            self.is_baby_seat = 'Without baby seat'
        self.color = color
        self.count_passenger_seats = count_passenger_seats

    def __str__(self):
        return f'Car: color = {self.color}, passenger seats = {self.count_passenger_seats}, ' \
               f'baby seat = {self.is_baby_seat}'


print(Car('black', 4, True, is_busy=False))
