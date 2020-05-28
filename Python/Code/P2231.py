# https://www.acmicpc.net/problem/2231
# https://www.acmicpc.net/source/20048394
N = int(input())

for i in range(N+2):
    count = i
    for j in str(count):
        count += int(j)
    if count == N:
        print(i)
        break
    elif i > N:
        print(0)
        break


