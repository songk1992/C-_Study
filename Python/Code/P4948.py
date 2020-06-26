# https://www.acmicpc.net/problem/4948


# 소수 리스트 작성
n = 123456 * 2
a = [False, False] + [True] * (n - 1)
primes = []

for i in range(2, n+1):
    if a[i]:
        primes.append(i)
        for j in range(2*i, n+1, i):
            a[j] = False
# print(primes)

# 테스트 케이스
while True:
    a = 0
    b = 0
    k = int(input())
    if k == 0:
        break
    elif k == 1:
        print(1)
    else:
        for i in range(len(primes)):
            if k >= primes[i]:
                a = i
            if 2 * k >= primes[i]:
                b = i
        print(b - a)
