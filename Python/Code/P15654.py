#https://www.acmicpc.net/problem/15654

#
from itertools import permutations
import sys
input = lambda : sys.stdin.readline().rstrip()

#입력
n, m = map(int, input().split())
list_n = list(map(int, input().split()))

#
list_n = sorted(list_n)

#
k = list(permutations(list_n, m))

#
for x in k:
    print(*x)
