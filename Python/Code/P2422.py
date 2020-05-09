
#https://www.acmicpc.net/problem/2422

#
from itertools import combinations
import sys
input = lambda : sys.stdin.readline().rstrip()

#입력
n, m = map(int, input().split())

# 2차원 배열에 조합이 앞뒤로 맛없는지 저장
ice_ = list(combinations(range(1, n+1), 3))
mat_ = [[0] * (n+1) for _ in range(n+1)]

for i in range(m):
    x, y = map(int, input().split())
    mat_[x][y] = 1
    mat_[y][x] = 1

#
ans = 0
for x in ice_:
    if mat_[x[0]][x[1]] or mat_[x[0]][x[2]] or mat_[x[1]][x[2]]:
        continue
    ans += 1
print(ans)

#
# set_list = []
# for _ in range(m):
#     set_list.append(set(map(int, input().split())))
#ice_cream_tuples = list(combinations(range(1, n+1), 3))
# ice_cream_list = [list(elem) for elem in ice_cream_tuples]


#
# check_list = ()
# k = len(ice_cream_list)
#
# for x in range(len(ice_cream_list)):
#     for y in range(len(set_list)):
#         check_list = set(ice_cream_list[x]) - set_list[y]
#         if len(check_list) == 1:
#             ice_cream_list[x] = [0]
#
# count = 0
# for x in range(len(ice_cream_list)):
#     if ice_cream_list[x] != [0]:
#         count += 1
# print(count)
