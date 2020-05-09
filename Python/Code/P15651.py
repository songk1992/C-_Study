


#https://www.acmicpc.net/problem/15656
from itertools import product
import sys
input = lambda : sys.stdin.readline().rstrip()


#입력
n, m = map(int, input().split())

#
k = list(product(range(1, n+1), repeat=m))

#
for x in k:
    print(*x)
