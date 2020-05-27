# https://www.acmicpc.net/problem/9095


# recursive solution

def n_made_of_123(arg):
    if arg == 0:
        count.append(1)
    elif arg == 1:
        count.append(1)
    elif arg == 2:
        count.append(1)
        count.append(1)
    elif arg > 2:
        temp3 = arg - 1
        temp4 = arg - 2
        temp5 = arg - 3
        n_made_of_123(temp3)
        n_made_of_123(temp4)
        n_made_of_123(temp5)

    return 0


T = int(input())
for _ in range(T):
    count = []
    n = int(input())
    n_made_of_123(n)
    print(sum(count))

# memorize intermediate results

