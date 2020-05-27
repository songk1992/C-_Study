# https://www.acmicpc.net/problem/11399

N = int(input())
array = list(map(int, input().split()))
array.sort(reverse=True)

waiting_time = 0
count = 1

for _ in array:
    waiting_time += _ * count
    count += 1
print(waiting_time)

