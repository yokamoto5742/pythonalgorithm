import csv

with open("st.csv", "r", newline="", encoding="utf-8") as f:
    r = csv.reader(f, delimiter=",")
    for row in r:
        print(",".join(row))
        print(row)
