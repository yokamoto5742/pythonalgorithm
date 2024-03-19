import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return self.radius ** 2 * math.pi

    def change_size(self, radius):
        self.radius = radius


circle = Circle(5123)
print(circle.area())
circle.change_size(10)
print(circle.area())
