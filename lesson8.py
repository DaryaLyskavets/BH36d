# Написать класс Rectangle

class Rectangle:

    def __init__(self, a: list[int], b: list[int], c: list[int], d: list[int]) -> None:
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        # точки a, b, c, d с координатами [x, y]

    def perimeter(self) -> int:
        distance_1 = ((self.a[0] - self.c[0]) ** 2 + (self.a[1] - self.c[1]) ** 2) ** 0.5
        distance_2 = ((self.a[0] - self.d[0]) ** 2 + (self.a[1] - self.d[1]) ** 2) ** 0.5
        perimeter = (distance_1 + distance_2) * 2
        return perimeter

    def square(self) -> int:
        distance_1 = ((self.a[0] - self.c[0]) ** 2 + (self.a[1] - self.c[1]) ** 2) ** 0.5
        distance_2 = ((self.a[0] - self.d[0]) ** 2 + (self.a[1] - self.d[1]) ** 2) ** 0.5
        square = distance_1 * distance_2
        return square


points = Rectangle(a=[3, -2], b=[-1, 4], c=[-1, -2], d=[3, 4])
points_2 = Rectangle(a=[4, -2], b=[-1, 5], c=[-1, -2], d=[4, 5])
print(points.perimeter())
print(Rectangle([8, -5], [3, 5], [3, -5], [8, 5]).square())
