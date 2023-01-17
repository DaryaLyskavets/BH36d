class Car:

    def __init__(self, color: str, count_passenger_seats: int, is_baby_seat: bool) -> None:
        self.is_busy = False
        self.is_baby_seat = is_baby_seat
        if is_baby_seat:
            self.is_baby_seat = 'yes'
        else:
            self.is_baby_seat = 'no'
        self.color = color
        self.count_passenger_seats = count_passenger_seats

    def __str__(self):
        return f'Car: color = {self.color}, passenger seats = {self.count_passenger_seats}, ' \
               f'baby seat = {self.is_baby_seat}'


cars = [Car(color='red', count_passenger_seats=2, is_baby_seat=True),
        Car('black', 3, is_baby_seat=False),
        Car('grey', 4, is_baby_seat=True),
        Car('white', 3, is_baby_seat=True)
        ]


class Taxi:

    def __init(self, cars: list[Car]):
        self.cars = cars

    def find_car(self, count_passengers: int, is_baby: bool) -> None:
        for i in cars:
            if count_passengers <= i.count_passenger_seats and is_baby == i.is_baby_seat and not i.is_busy:
                i.is_busy = not i.is_busy
                return i

car = Taxi()
print(car.find_car(3, 'yes'))
print(car.find_car(3, 'yes'))
print(car.find_car(3, 'yes'))