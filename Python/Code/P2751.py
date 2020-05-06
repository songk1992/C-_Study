#수정렬하기
#https://www.acmicpc.net/problem/2751

import sys
input = lambda : sys.stdin.readline().rstrip()

N = int(input())

Number = []

for _ in range(N):
    Number.append(int(input()))

Number.sort()
for x in range(N):
    print(Number[x])
