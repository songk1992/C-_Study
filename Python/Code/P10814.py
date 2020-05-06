#나이순 정렬
#https://www.acmicpc.net/problem/10814

import sys
input = lambda : sys.stdin.readline().rstrip()

# N of members
N = int(input())

#
member_details = []

# input
for _ in range(N):
    age, name = input().split()
    member_details.append([int(age), name])

#
member_details.sort(key=lambda x:(x[0]))
for x in member_details:
    print(x[0], x[1])
