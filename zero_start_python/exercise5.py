def print_hello(count):
    for i in range(count):
        print("Hello")


def get_rectangle_area(width, height):
    return width * height


def get_message(name):
    return f'こんにちは、{name}さん'


def get_absolute_value(value):
    return abs(value)


def get_tail(*args):
    return args[-1]


# print_hello 関数を呼び出し、2回 "Hello" を表示します。
print_hello(2)

# get_rectangle_area 関数を呼び出し、幅4、高さ5の長方形の面積を計算し表示します。
print(get_rectangle_area(4, 5))

# get_message 関数を呼び出し、名前を引数にして挨拶メッセージを表示します。
print(get_message("太郎"))

# get_absolute_value 関数を呼び出し、-10 の絶対値を表示します。
print(get_absolute_value(-100000))

# get_tail 関数を呼び出し、引数のリストから最後の要素を表示します。
print(get_tail(1, 2, 3))
