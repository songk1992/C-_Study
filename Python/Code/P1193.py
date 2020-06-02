# https://www.acmicpc.net/problem/1193

N = int(input())
Counter = N

if N == 1:
    print("1/1")
    exit()
if N == 2:
    print("1/2")
    exit()

for _ in range(N):
    AS = (_ + _ ** 2)//2
    if N <= AS:
        Counter -= ((_-1) + (_-1) ** 2)//2
        if _ % 2 == 0:
            print("{}/{}".format(Counter, _ +1 - Counter))
        else:
            print("{}/{}".format(_ +1 - Counter, Counter))
        break
