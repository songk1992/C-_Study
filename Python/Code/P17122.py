# https://www.acmicpc.net/problem/17122
# 풀고나서 배운 인상깊은 코드 https://www.acmicpc.net/source/18571303

array_of_letters = "ABCDEFGH"
array_of_numbersA = "12345678"

ChessBoardA = [[] for _ in range(64)]
ChessBoardB = [[] for _ in range(64)]
count = 0


for i in range(8):
    for j in range(8):
        colour = (i+j) % 2
        ChessBoardA[count].append(str(array_of_letters[i]+array_of_numbersA[j]))
        ChessBoardA[count].append(colour)
        ChessBoardB[count].append(str(count+1))
        ChessBoardB[count].append(colour)
        count += 1

T = int(input())
for _ in range(T):
    A, B = input().split()
    for _ in range(64):
        if A == ChessBoardA[_][0]:
            Check_A = ChessBoardA[_][1]
            continue
    for _ in range(64):
        if B == ChessBoardB[_][0]:
            Check_B = ChessBoardB[_][1]
            continue
    if Check_A == Check_B:
        print('YES')
    else:
        print('NO')
# print(ChessBoardA)
# print(ChessBoardB)
