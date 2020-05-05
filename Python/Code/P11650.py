#https://www.acmicpc.net/problem/11650

test_case_value = int(input())
coordinates = []

for i in range(test_case_value):
    coordinates.append(list(map(int, input().split())))

    # x, y = input().split()
    # x = int(x)
    # y = int(y)
    # coordinates[i].append((x, y))

coordinates = sorted(coordinates, key = lambda x : (x[0], x[1]))
# for i in range(test_case_value):
#     for j in range(i+1, test_case_value):
#         if i == j:
#             continue
#
#         c1 = coordinates[i]
#         c2 = coordinates[j]
#
#         if c1[0] > c2[0]:
#             temp = coordinates[i]
#             coordinates[i] = coordinates[j]
#             coordinates[j] = temp
#
#         elif (c1[0] == c2[0]) and (c1[1] > c2[1]):
#             temp = coordinates[i]
#             coordinates[i] = coordinates[j]
#             coordinates[j] = temp


for [i, j] in coordinates:
    print(i, j)
#print(coordinates)
