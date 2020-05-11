#https://www.acmicpc.net/problem/15656


#
from itertools import product
import sys
input = lambda : sys.stdin.readline().rstrip()

#입력
n, m = map(int, input().split())
list_n = list(map(int, input().split()))

#
list_n = sorted(list_n)

#
k = list(product(list_n, repeat=m))

#
for x in k:
    print(*x)
