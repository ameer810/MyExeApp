# rows = int(input("write num of rows :"))
# count = 0
# count2 = rows
# gg = False
# for i in range(0, rows):
#     if i == int(rows / 2) + 1:
#         print(' ' * (int(rows / 2)) + '*' * rows)
#         count = rows - 1
#         count2 = int(count / 2) + 1
#         gg = True
#     for j in range(0, count):
#         if j == 0:
#             print(' ' * count2, end='')
#         else:
#             print('*', end="")
#     print()
#     if not gg:
#         count += 2
#         count2 -= 1
#     else:
#         count -= 2
#         count2 += 1
# pepole=[
#     {'s':3},
#     {'d':'h'},
#     {'k':'l'},
#     {'r':'e'},
#     {'ded':'de'}
# ]
# taller_than_60=0
# for person in pepole:
#     if person['height']>=60:
#         taller_than_60+=1
# print(len(pepole))
# numbers=[1.34,2.98]
# for i in range(len(numbers)):
#     rounded_value=round(numbers[i])
#     numbers[i] = rounded_value
# print(numbers)
k=0
for i in range(1,10):
    k+=1
print(k)