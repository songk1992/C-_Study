#https://www.acmicpc.net/problem/15652

#
from itertools import combinations_with_replacement as cwr_function
import sys
input = lambda : sys.stdin.readline().rstrip()

#입력
n, m = map(int, input().split())


#
k = list(cwr_function(range(1, n+1), m))

#
for x in k:
    print(*x)
