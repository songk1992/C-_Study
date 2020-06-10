# https://www.acmicpc.net/problem/10250

def HotelRoom(h, w, n):
    b = n // h + 1
    a = n % h
    if a == 0:
        a = h
        b -= 1

    if b < 10:
        b = str(0) + str(b)
    print(str(a)+str(b))

T = int(input())

for _ in range (T):
    H, W, N = map(int, input().split())
    HotelRoom(H, W, N)
