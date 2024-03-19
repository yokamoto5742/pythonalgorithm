total = 10

for i in range(10, 21):
    if i == 15:
        continue
    else:
        print(total, end=" ")
        i = i + 1
        total = total + i

# total = 10
# i = 10
#
# while i < 21:
#     if i == 15:
#         break
#     else:
#         print(total, end=" ")
#         i = i + 1
#         total = total + i
