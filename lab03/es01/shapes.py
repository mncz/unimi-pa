import math

class EquilateralTriangle:
    def __init__(self, side: int):
        self.__side = side

    def calculate_area(self):
        return round(math.sqrt(3) / 4 * self.__side ** 2, 2)

    def calculate_perimeter(self):
        return self.__side * 3

class Circle:
    def __init__(self, radius: int):
        self.__radius = radius

    def calculate_area(self):
        return round(self.__radius ** 2 * math.pi, 2)

    def calculate_perimeter(self):
        return round(self.__radius * 2 * math.pi, 2)

class Rectangle:
    def __init__(self, side1: int, side2: int):
        self.__side1 = side1
        self.__side2 = side2

    def calculate_area(self):
        return round(self.__side1 * self.__side2, 2)

    def calculate_perimeter(self):
        return (self.__side1 + self.__side2) * 2

class Square:
    def __init__(self, side: int):
        self.__side = side

    def calculate_area(self):
        return round(self.__side ** 2, 2)

    def calculate_perimeter(self):
        return self.__side * 4

class Pentagon:
    def __init__(self, side: int):
        self.__side = side

    def calculate_area(self):
        apothem = self.__side / (2 * math.tan(math.pi / 5))
        return round((5 * self.__side * apothem) / 2, 2)

    def calculate_perimeter(self):
        return self.__side * 5
