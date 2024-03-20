class Apple:
    def __init__(self, w, c, s, p):
        self.weight = w
        self.color = c
        self.size = s
        self.price = p
        print("インスタンスを作成しました!")


apple = Apple("150g", "red", "big", "200円")
print(apple.weight)
print(apple.color)
print(apple.size)
print(apple.price)
