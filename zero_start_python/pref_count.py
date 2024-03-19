pref_count_dict = {}

with open('visitor_record.txt', 'r', encoding='utf-8') as f:
    for line in f:
        date, pref, num_adults, num_children = line.split(',')  # 1行をカンマで分割して変数に格納
        num_all = int(num_adults) + int(num_children)

        if pref in pref_count_dict:
            pref_count_dict[pref] += num_all
        else:
            pref_count_dict[pref] = num_all


# リストやタプルの2番目の要素（item[1]）を返す関数
def get_second_element(item):
    return item[1]


# 辞書の項目を値の降順にソート
pref_count_sorted = sorted(pref_count_dict.items(), key=get_second_element, reverse=False)

for i in pref_count_sorted:
    print(i[0], f'{i[1]}名')
