class MakeTwoValue:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def two_value(self):
        if self.x == self.y:
            return True
        else:
            return False


make_two_value = MakeTwoValue(10, 10)
print(make_two_value.two_value())

make_two_value = MakeTwoValue(10, 20)
print(make_two_value.two_value())


def compare(obj1, obj2):
    return obj1 is obj2


print(compare(10, 10))
print(compare(10, 20))