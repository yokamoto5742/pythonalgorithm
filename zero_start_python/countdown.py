def countdown(start=10, end=0):
    print('1つめの引数で受け取った値:', start)
    print('2つめの引数で受け取った値:', end)
    print('カウントダウン開始!')
    i = start
    while i >= end:
        print(i)
        i = i - 1
    print('カウントダウン終了!')


countdown(100, 11)
countdown()
