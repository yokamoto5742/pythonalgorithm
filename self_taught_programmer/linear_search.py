def linear_search(number_list, n):
    found = False
    for i in number_list:
        if i == n:
            found = True
            break
    return found


number_list = range(1, 101)
n = 5
print(linear_search(number_list, n))
n = 105
print(linear_search(number_list, n))
