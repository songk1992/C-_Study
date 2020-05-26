# https://www.acmicpc.net/problem/1463

# memorize intermediate results / 메모리 초과

# import sys
# sys.setrecursionlimit(10**6)
#
# def OP(n):
#     print(arr)
#     if arr[n] != 'u':
#         return arr[n]
#     elif n == 1:
#         result = 0
#     else:
#         temp1 = 999999
#         temp2 = 999999
#         temp3 = 999999
#         if n % 3 == 0:
#             temp1 = OP(n//3)
#         if n % 2 == 0:
#             temp2 = OP(n//2)
#         if n > 1:
#             temp3 = OP(n-1)
#         result = min(temp1, temp2, temp3)
#         result += 1
#
#     arr[n] = result
#     return result
#
#
# N = int(input())
# arr = ['u' for _ in range(N+1)]
# print(OP(N))

# recursive solution
# https://chunghyup.tistory.com/49

def f(arg):
    temp_list = []
    for _ in arg:
        if _ % 2 == 0:
            temp_list.append(_//2)
        if _ % 3 == 0:
            temp_list.append(_//3)
        temp_list.append(_ - 1)
    return temp_list


N = int(input())
count = 0
minimum_list = [N]

while True:
    if N == 1:
        print(count)
        break
    minimum_list = f(minimum_list)
    count += 1
    if min(minimum_list) == 1:
        print(count)
        break

