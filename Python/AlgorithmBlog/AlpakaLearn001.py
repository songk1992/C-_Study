
#**********************************************************
#https://m.blog.naver.com/wpghks7/221584113312
#https://github.com/LeeJehwan

#위에 링크를 보고 학습목적으로 따라함

# 입력을 한 줄씩 통째로 받아서 a에 문자열로 저장
a = input()

# 입력을 한줄씩 a에 정수로 저장
a = int(input())

# 입력을 공백(white spacing) 자르고 저장 하지만 원소는 인트가 아님
a = int().split()

# map 을 사용하면 map(func, x)일때 각원소 x에 func 일일이 적용해줌
a = map(int, input().split())

#입력이 1 2 3일경우 각 변수 a,bc에 각각 저장
a, b, c = map(int,input().split())


# n을 입력받고 n개의 수를 입력받는 경우
# e.g) 5 1 2 3 4 5
a, *b = map(int, input().split())

#e.g)
while True:
    a, *b = map(int, input().split())
    if a == 0:
        break

#**********************************************************

# 1차원 배열 초기화된 배열 10개
a = list()
for _ in range(10):
    a.append(0)
# 1차원 배열 초기화된 배열 10개 간단
a = [0 for _in range(10)]

# 1차원 배열 초기화된 배열 10개 더 간단
a =[0] * 10

#**********************************************************

# n x m 배열
a = [[0] * m for _ in range(n)]


#**********************************************************

#다섯줄에 걸쳐서 L,A,B,C,D 입력받기
L, A, B, C, D = [int(input())for _ in range(5)]

#**********************************************************

# 2차원 배열
# 붙어 있는 경우
# ex)
# 4 6
# 101111
# 101010
# 101011
# 111011

n, m = map(int, input().split())
a = [list(map(int, input())) for _ in range(n)]

# 떨어진 경우
# ex)
# 4 6
# 1 0 1 1 1 1
# 1 0 1 0 1 0
# 1 0 1 0 1 1
# 1 1 1 0 1 1

n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

#**********************************************************

#빠른 input

import sys
a =
sys.stdin.readline().rstrip()

import sys
input = lambda:
    sys.stdin.readline().rsstrip()
