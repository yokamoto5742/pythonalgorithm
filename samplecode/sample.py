def even_odd(num):
    """
    偶数か奇数かを判定する関数
    :param num: int
    :return: None (print)
    """
    if num % 2 == 0:
        return print(f"{num}は偶数です")
    else:
        return print(f"{num}は奇数です")


if __name__ == "__main__":
    num1 = int(input("数字を入力してください:"))
    even_odd(num1)
