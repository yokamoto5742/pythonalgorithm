from io import UnsupportedOperation

f = open('some.txt', 'r')
try:
    f.write('Hello, World!')
except UnsupportedOperation as e:
    print(f'例外が発生しました:{e}')
finally:
    print('ファイルをクローズします')
    f.close()


raise ValueError('不正な引数です')
