# https://www.acmicpc.net/problem/16396

def DrawLine(arg1, arg2):
    for _ in range(arg1, arg2):
        arr[_] = 1

T = int(input())
arr = [0 for _ in range(10000)]

for _ in range(T):
    n1, n2 = map(int, input().split())
    DrawLine(n1, n2)

print(sum(arr))
