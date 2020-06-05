# https://www.acmicpc.net/problem/1003



Max_val = 50
list = [[0, 0] for _ in range(Max_val)]
list[0] = [1, 0]
list[1] = [0, 1]
for j in range(2, Max_val):
    list[j][0] = list[j-1][0] + list[j-2][0]
    list[j][1] = list[j-1][1] + list[j-2][1]

T = int(input())
for _ in range(T):
    N = int(input())
    print("{} {}".format(list[N][0], list[N][1]))

# def fibonacci(arg):
#     if arg == 0:
#         C_0.append(1)
#         return 0
#     elif arg == 1:
#         C_1.append(1)
#         return 1
#     else:
#         return fibonacci(arg - 1) + fibonacci(arg - 2)
#
#
# T = int(input())
#
# for _ in range(T):
#     C_0 = []
#     C_1 = []
#     N = int(input())
#     fibonacci(N)
#     print(len(C_0), len(C_1))
