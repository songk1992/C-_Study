
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
k = 0

for _ in a:
    k += sum(_)
print(k)
