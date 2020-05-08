https://www.acmicpc.net/problem/15650


from itertools import combinations
# from itertools import combinations
# import sys
# input = lambda : sys.stdin.readline().rstrip()

n, m = map(int, input().split())
# N, M = map(int, input().split())


c = list(combinations(range(1, n+1), m))
# list_a = []
# for x in range(N):
#     list_a.append((x+1))
# list_p = list(combinations(list_a, M))

for x in c:
    print(*x)
# for x in list_p:
#     print(*x)

