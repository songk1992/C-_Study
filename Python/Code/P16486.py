# https://www.acmicpc.net/problem/16486

from _collections import deque
import sys
input = lambda: sys.stdin.readline().rstrip()

pi = 3.141592
d1 = int(input())
d2 = int(input())
circumference = (3.141592 * d2 + d1) * 2
print(circumference)
