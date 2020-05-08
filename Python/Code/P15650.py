https://www.acmicpc.net/problem/15650

from itertools import combinations
import sys
input = lambda : sys.stdin.readline().rstrip()

N, M = map(int, input().split())
list_a = []

for x in range(N):
    list_a.append((x+1))

list_p = list(combinations(list_a, M))

for x in list_p:
    print(*x)
