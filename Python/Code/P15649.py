
#https://www.acmicpc.net/problem/15649

#
from itertools import permutations
import sys
input = lambda : sys.stdin.readline().rstrip()

#입력
n, m = map(int, input().split())

#
k = list(permutations(range(1, n+1), m))

#
for x in k:
    print(*x)
