# https://www.acmicpc.net/problem/3052

L = []
for _ in range(10):
    L.append(int(input()) % 42)
print(len(set(L)))
