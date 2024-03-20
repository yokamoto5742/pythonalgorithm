import re

text = """キリンは大昔から__複数名詞__の興味の対象でした。キリンは__複数名詞__の中で一番背が高いですが、科学者たちはそのような長い__体の一部__をどうやって獲得したのか説明できません。キリンの身長は__数値__m近くあり、その高さのほとんどは脚と__体の一部__によるものです。"""


def mad_libs(mls):
    hints = re.findall("__.*?__", mls)
    if hints is not None:
        for word in hints:
            q = "{}を入力してください: ".format(word)
            new = input(q)  # ユーザーの入力を直接newに格納
            mls = mls.replace(word, new, 1)
        mls = mls.replace("\n", " ")
        print("\n" + mls)  # 結果を表示
    else:
        print("{}は無効な引数です".format(mls))


mad_libs(text)
