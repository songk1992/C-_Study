# https://www.acmicpc.net/problem/1110

N = int(input())
count = 0
temp = N
while True:
    # print("N : ", N)
    if N < 10:
        N = N * 11
    else:
        temp2 = int(str(N)[0]) + int(str(N)[1])
        if temp2 < 10:
            N = 10 * int(str(N)[1]) + temp2
        else:
            N = 10 * int(str(N)[1]) + int(str(temp2)[1])
    count += 1
    if temp == N:
        print(count)
        break
