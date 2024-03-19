class X:
    def __init__(self):
        print('[x]')

    def a(self):
        print('[x.a]')

    def b(self):
        print('[x.b]')


class Y(X):
    def __init__(self):
        super().__init__()
        print('[y]')

    def a(self):
        print('[y.a]')
        super().a()


if __name__ == '__main__':
    x = X()  # Xのインスタンスを生成し、'[x]'が出力される。
    x.a()  # '[x.a]'が出力される。
    x.b()  # '[x.b]'が出力される。
    y = Y()  # Yのインスタンスを生成する。まずXの__init__が呼ばれて'[x]'が、次にYの__init__で'[y]'が出力される。
    y.a()  # '[y.a]'が出力され、その後super().a()によって'[x.a]'が出力される。
    y.b()  # Yにはbメソッドが定義されていないため、継承されたXのbメソッドが呼ばれて'[x.b]'が出力される。
