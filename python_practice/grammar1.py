from grammar import py2_or_py3


class PracticeBookError(Exception):
    pass


x, y, r = 1, 2, 3
print(x)
print(y)
print(r)

if __name__ == '__main__':
    py2_or_py3()
