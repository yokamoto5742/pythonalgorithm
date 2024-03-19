class Shape:
    def __init__(self, w, l):
        self.width = w
        self.len = l

    def print_size(self):
        print("{} by {}".format(self.width, self.len))


class Square(Shape):
    square_list = []

    def __init__(self, w, l):
        super().__init__(w, l)
        self.square_list.append((self.width, self.len))

    def calculate_perimeter(self):
        return self.width * 2 + self.len * 2

    def __repr__(self):
        return "{} by {} by {} by {}".format(
            self.width, self.len, self.width, self.len)


square = Square(29, 29)

print(square)
