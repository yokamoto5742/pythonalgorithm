a = 10


def function_a():
    print('function_a()の処理が呼び出されました!')
    global a
    a = 20


def function_b():
    print('function_b()の処理が呼び出されました!')
    function_a()
    print('function_b()の処理が終了しました!')

print(a)
function_b()
function_a()
print(a)
