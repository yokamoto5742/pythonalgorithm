total = 0

for i in range(100):
    if i % 4 != 0:
        continue
    print(i, total)
    total = total + i

print('4の倍数の合計は', total)
