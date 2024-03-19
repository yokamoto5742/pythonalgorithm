class Person:
    def __init__(self, name):
        self.name = name


bob = Person('bob')
same_bob = bob
print(bob is same_bob)  # True

another_bob = Person('bob')
print(bob is another_bob)  # False


x = 10
if x is None:
    print("x is None")
else:
    print("x is not None")

x = None
if x is None:
    print("x is None")
else:
    print("x is not None")
