# https://www.acmicpc.net/problem/10996
n = int(input())
for _ in range(2 * n):
    for i in range(n):
        if (_+i) % 2 == 0:
            print("*", end="")
        else:
            print(" ", end="")
    print()
