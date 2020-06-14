# https://www.acmicpc.net/problem/2775
# https://www.acmicpc.net/source/20200643

arr = [[0] * 15 for _ in range(15)]
for _ in range(15):
    arr[0][_] = _ + 1

for i in range(1, 15):
    for j in range(15):
        for k in range(j+1):
            arr[i][j] += arr[i-1][k]
for _ in range(int(input())):
    room_floor = int(input())
    room_number = int(input())
    if room_number == 0:
        print(0)
    else:
        print(arr[room_floor][room_number-1])

