import random

def hangman(word):
    wrong = 0
    stages = ["",
              "________        ",
              "|               ",
              "|        |      ",
              "|        0      ",
              "|       /|\     ",
              "|       / \     ",
              "|               "
              ]
    rletterts = list(word)
    board = ["_"] * len(word)
    win = False
    print("ハングマンへようこそ！")


    while wrong < len(stages) - 1:
        print("\n")
        msg = "1文字を予想してください"
        char = input(msg)
        if char in rletterts:
            cind = rletterts.index(char)
            board[cind] = char
            rletterts[cind] = '$'
        else:
            wrong += 1
        print(" ".join(board))
        e = wrong + 1
        print("\n".join(stages[0:e]))
        if "_" not in board:
            print("あなたの勝ち！")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages[0:wrong+1]))
        print("あなたの負け！正解は{}".format(word))


if __name__ == "__main__":
    words = random.choice(["cat", "dog", "bird", "fish", "elephant"])
    hangman(words)
