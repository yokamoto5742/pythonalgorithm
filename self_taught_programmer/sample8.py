x = 10
while x > 0:
    if x == 5 or x == 3:
        x -= 1  # この行をif文の内部に移動して、xの値を減少させます。
        continue
    print("{}".format(x))
    x -= 1

print("Happy New Year!!")


qs = ["What is your name?", "What is your fav. color?", "What is your quest?"]
n = 0
while True:
    print("Type q to quit")
    a = input(qs[n])
    if a == "q":
        break
    n = (n + 1) % 3
