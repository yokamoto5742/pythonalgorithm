items = [1, 2, 3, 4, 5]
for i in items:
    print(f'変数iの値は{i}です。')

print(items)

for i in range(1, 6):
    print(f'{i}番目の処理です。')

chars = 'World!'
for count, char in enumerate(chars):
    print(f'{count}番目の文字は{char}')
