# https://www.acmicpc.net/problem/11047

N, K = map(int, input().split())
array = []

for _ in range(N):
    temp_value = int(input())
    array.append(temp_value)
array.sort(reverse=True)

count = 0
for _ in array:
    if K >= _:
        temp_value = K // _
        count += temp_value
    K = K % _

print(count)
