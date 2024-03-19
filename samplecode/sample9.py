answer = ["q", "Q"]
letter = input("文字を入力してください:")

# リストを使って 'q' または 'Q' のいずれかであるかをチェックします
while letter not in answer:
    print("{}はハズレです。".format(letter))
    letter = input("文字を入力してください:")

print("正解!")
