movie =[["トップガン", "Risky Business", "Minority Report"], ["たいたにっく", "The Revenant", "Inception"],
 ["Training Day", "Man on Fire", "飛行"]]

with open("movies.csv", "w", encoding="cp932") as file:
    for i in range(len(movie)):
        file.write(",".join(movie[i]) + "\n")

print("ファイルに書き込みました。")