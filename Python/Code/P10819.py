# #내답
#
# from itertools import permutations as pm
#
# n = int(input())
# p = list(map(int, input().split()))
#
# p = list(pm(p))
#
# k = len(p)
# sum = 0
# max = 0
#
#
# list_k = []
# for i in range(len(p)):
#     list_k.append(list(p[i]))
#
# for i in range(k):
#     for j in range(n-1):
#         sum += abs(list_k[i][j]-list_k[i][1+j])
#
#     if(max<sum):
#         max = sum
#     sum = 0
#
# print(max)

#출처코드
#https://m.blog.naver.com/wpghks7/221585604878

from itertools import permutations
import sys
input = lambda : sys.stdin.readline().rstrip()

n = int(input())
a = list(map(int, input().split()))
p = list(permutations(a))

ans = 0
for x in p:
    total = 0
    for i in range(n-1):
        total += abs(x[i] - x[i+1])
    ans = max(ans, total)
print(ans)
