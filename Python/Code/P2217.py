# https://www.acmicpc.net/problem/2217
# 흥미로운 답안 https://www.acmicpc.net/source/19949322

N = int(input())
array = []
weight_capacity = 0
count = 0

for _ in range(N):
    array.append(int(input()))
array.sort(reverse=True)

for _ in array:
    count += 1
    current_capacity = _ * count
    if weight_capacity < current_capacity:
        weight_capacity = current_capacity

print(weight_capacity)


# 시간 초과 / 재귀법
# import sys
# sys.setrecursionlimit(10**5)
#
# def f(arg_list, temp_value1):
#     if not arg_list:
#         return temp_value1
#     temp_array.append((arg_list.pop()))
#     temp_value2 = min(temp_array) * len(temp_array)
#     if temp_value1 < temp_value2:
#         temp_value1 = temp_value2
#     result = f(arg_list, temp_value1)
#     return result
#
#
# N = int(input())
# array = []
# temp_array = []
#
# for _ in range(N):
#     array.append(int(input()))
# array.sort(reverse=True)
#
# print(f(array, 0))
