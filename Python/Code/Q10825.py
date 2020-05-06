#https://www.acmicpc.net/problem/10825

import sys
input = lambda : sys.stdin.readline().rstrip()

# N of students
N = int(input())

# Korean, English, Math
ClassTestResult = []

for _ in range(N):
    name, kor, eng, math = input().split()
    ClassTestResult.append([name, int(kor), int(eng), int(math)])

ClassTestResult.sort(key=lambda x:(-x[1],x[2],-x[3],x[0]))
for x in ClassTestResult:
    print(x[0])
