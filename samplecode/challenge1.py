weather = input("今日の天気はどうですか?: ")

with open("weather.txt", "w", encoding="utf-8") as file:
    file.write(weather)

print("回答をファイルに書き込みました。")
