#내답

# from itertools import permutations
#
# N = int(input())
# my_list = []
#
# for _ in range(N):
#     my_list.append(_+1)
#
# new_list = list(permutations(my_list))
# K = len(new_list)
#
#
# for i in range(K):
#     for j in range(N):
#         print(new_list[i][j], end=" ")
#         if (j == N-1) and (i != K-1):
#             print("")

# 출처의 답
# https://m.blog.naver.com/wpghks7/221585604878

from itertools import permutations as pm
n = int(input())
p = list(pm(range(1, n+1)))
for x in p:
    print(*x)
