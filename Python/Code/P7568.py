# https://www.acmicpc.net/problem/7568
T = int(input())
arr = []
check = [1 for _ in range(T)]


for _ in range(T):
    k = list(map(int, input().split()))
    arr.append(k)

for i in range(T):
    for j in range(T):
        if i == j:
            continue
        if arr[i][0] < arr[j][0] and arr[i][1] < arr[j][1]:
            check[i] += 1
for x in check:
    print(x, end=" ")

