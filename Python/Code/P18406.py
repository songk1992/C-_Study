
#https://www.acmicpc.net/problem/18406
str_N = (input())
Length_N = len(str_N)
int_N = int(str_N)

if (Length_N % 2) == 0:
    count = 0
    for _ in range(Length_N):
        if int(_) < Length_N/2:
            count += int(str_N[_])
        else:
            count -= int(str_N[_])
    if count == 0:
        print("LUCKY")
        exit()
print("READY")
