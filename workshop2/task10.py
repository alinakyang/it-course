import math


class Circle:
    @staticmethod
    def conversion_from_meters_to_centimeters(m):
        return 100 * m

    @staticmethod
    def conversion_from_centimeters_to_meters(cm):
        return cm / 100

    def __init__(self, radius):
        self.radius = radius

    def get_len(self):
        return 2 * math.pi * self.radius

    def get_square(self):
        return math.pi * self.radius * self.radius


obj = Circle(2.55)
print(obj.get_len(), obj.get_square())
print(obj.conversion_from_meters_to_centimeters(1))
