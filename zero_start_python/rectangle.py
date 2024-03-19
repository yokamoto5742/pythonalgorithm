class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height

    def is_large(self, rect):
        return self.get_area() > rect.get_area()

    def compare_area(self, rect):
        if self.get_area() > rect.get_area():
            return 'larger'
        elif self.get_area() < rect.get_area():
            return 'smaller'
        else:
            return 'equal'

r0 = Rectangle(40, 30)
r1 = Rectangle(30, 40)

print('r0の面積:', r0.get_area())
print('r1の面積:', r1.get_area())

comparison_result = r0.compare_area(r1)
if comparison_result == 'larger':
    print('r0の面積の方が大きい')
elif comparison_result == 'smaller':
    print('r1の面積の方が大きい')
else:
    print('r0とr1の面積は同じです')
