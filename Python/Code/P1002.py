#https://www.acmicpc.net/problem/1002

T = int(input())

for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    distance1 = r1 + r2
    distance2 = ((x2 - x1)**2 + (y2 - y1)**2)**0.5

    if x1 == x2 and y1 == y2:
        if r1 == r2:
            print(-1)
        else:
            print(0)

    elif distance1 < distance2:
        print(0)

    elif distance1 == distance2:
        print(1)

    elif distance1 > distance2:
        t1 = max(r1, r2)
        t2 = min(r1, r2)
        if distance2 + t2 < t1:
            print(0)
        elif distance2 + t2 == t1:
            print(1)
        elif distance2 + t2 > t1:
            print(2)
