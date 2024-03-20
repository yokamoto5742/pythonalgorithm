from collections import Counter


def count_strings(strings):
    count_dict = {}
    for string in strings:
        if string in count_dict:
            count_dict[string] += 1
        else:
            count_dict[string] = 1
    print(count_dict)


count_strings("hello hold")

print(Counter("こんばんは"))
