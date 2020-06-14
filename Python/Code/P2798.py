# https://www.acmicpc.net/problem/2798
# https://www.acmicpc.net/source/20339293

N, M = map(int, input().split())
arr = list(map(int, input().split()))
d = 0

for i in range(N):
    for j in range(N):
        if i == j:
            continue
        for k in range(N):
            if i == k or j == k:
                continue
            a = arr[i] + arr[j] + arr[k]
            if a > M:
                continue
            d = max(d, a)
print(d)
