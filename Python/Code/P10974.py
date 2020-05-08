#https://www.acmicpc.net/problem/10974
from itertools import permutations

N = int(input())
my_list = []

for _ in range(N):
    my_list.append(_+1)

new_list = list(permutations(my_list))
K = len(new_list)


for i in range(K):
    for j in range(N):
        print(new_list[i][j], end=" ")
        if (j == N-1) and (i != K-1):
            print("")
