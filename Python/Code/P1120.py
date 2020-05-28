# https://www.acmicpc.net/problem/1120


def checker(a, b):
    count = 50
    for i in range(len(b)):
        if i + len(a) > len(b):
            break
        temp = 0
        for j in range(len(a)):
            if a[j] != b[j + i]:
                temp += 1
        count = min(temp, count)
    print(count)
    return 0


A, B = input().split()
checker(A, B)
