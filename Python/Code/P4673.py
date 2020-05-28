# https://www.acmicpc.net/problem/4673

# 64ms 답안 신기해서 추가 https://www.acmicpc.net/source/20066138
N = 10000

for num in range(N):
    digit = len(str(num))
    count = 0

    if 0 <= num < 9:
        if num % 2 == 0:
            continue
        else:
            print(num)
    elif 9 < num < 20:
        continue
    else:
        for i in range(num - (digit * 9), num + 1):
            if int(i) + sum(int(n) for n in str(i)) == num:
                count += 1
                break

        if count == 0:
            print(num)
