
#https://www.acmicpc.net/problem/15953

#prize
prize_2017 = [0 for _ in range(21)]

prize_2017[0] = 500
for _ in range(1, 3):
    prize_2017[_] = 300
for _ in range(3, 6):
    prize_2017[_] = 200
for _ in range(6, 10):
    prize_2017[_] = 50
for _ in range(10, 15):
    prize_2017[_] = 30
for _ in range(15, 21):
    prize_2017[_] = 10
# print(prize_2017)

prize_2018 = [0 for _ in range(31)]
prize_2018[0] = 512
for _ in range(1, 3):
    prize_2018[_] = 256
for _ in range(3, 7):
    prize_2018[_] = 128
for _ in range(7, 15):
    prize_2018[_] = 64
for _ in range(15, 31):
    prize_2018[_] = 32
# print(prize_2018)

#
T = int(input())

for _ in range(T):
    a, b = map(int, input().split())

    if 0 < a < 22:
        a = prize_2017[a-1]
    else:
        a = 0
    if 0 < b < 32:
        b = prize_2018[b-1]
    else:
        b = 0
    print(a*10000 + b*10000)
