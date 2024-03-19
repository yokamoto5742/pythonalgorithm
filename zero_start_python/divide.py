print('a ÷ b を計算します')
try:
    a = int(input('aの値を入力してください: '))
    b = int(input('bの値を入力してください: '))
    c = float(a / b)
    print('答えは', c)
except ValueError as ex:
    print('入力が数値ではありません')
    print(ex)
except ZeroDivisionError:
    print('0で割ることはできません')
else:
    print('正常に計算しました')
finally:
    print('プログラムを終了します')
