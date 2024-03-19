class Rectangle:
    recs = []

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.recs.append((self.width, self.height))

    def print_size(self):
        print('{} by {}'.format(self.width, self.height))


r1 = Rectangle(10, 24)
r2 = Rectangle(20, 40)
r3 = Rectangle(100, 200)

print(Rectangle.recs)