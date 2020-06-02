# https://www.acmicpc.net/problem/1316


def GroupChecker (arg_string):
    Check = []
    arg_array = list(arg_string)
    while arg_array:
        now = arg_array.pop(0)
        if (now in Check) and (previous != now):
            return -1
        else:
            Check.append(now)
        previous = now
    return 0


N = int(input())
Counter = N

for _ in range(N):
    GivenString = input()
    Counter += GroupChecker(GivenString)
print(Counter)
