https://www.acmicpc.net/problem/6603

from itertools import combinations

permutation_list =[]


while True:
    k, *S = input().split()

    permutation_list = S
    if k == '0':
        break
    for i in combinations(permutation_list, 6):
        print(" ".join(i))
    print()


#
#     for a1 in range(len(S)):
#         for a2 in range(len(S)):
#             if a2 == a1:
#                 continue
#             for a3 in range(len(S)):
#                 if a3 == a2 or a3 == a1:
#                     continue
#                 for a4 in range(len(S)):
#                     if a4 == a3 or a4 == a2 or a4 == a1:
#                         continue
#                     for a5 in range(len(S)):
#                         if a4 == a5 or a5 == a3 or a5 == a2 or a5 == a1:
#                             continue
#                         for a6 in range(len(S)):
#                             if a6 == a5 or a6 == a4 or a6 == a3 or a6 == a2 or a6 == a1:
#                                 continue
#                             permutation_list.append(sorted([S[a1], S[a2], S[a3], S[a4], S[a5], S[a6]]))
#
#     permutation_list.sort()
#     set_list = list(set(map(tuple, permutation_list)))
#     permutation_list = list(set_list)
#     permutation_list.sort()
#
#     for x1, x2, x3, x4, x5, x6 in permutation_list:
#         print(x1, x2, x3, x4, x5, x6)
#     print("\n")


