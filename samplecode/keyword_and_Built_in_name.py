import keyword

print(keyword.kwlist)

# 組み込み名のリストを取得
builtins = dir(__builtins__)

for name in builtins:
    print(name)

