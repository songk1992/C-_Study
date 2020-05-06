
#https://www.acmicpc.net/problem/1431
#시리얼번호 정렬

import sys
input = lambda : sys.stdin.readline().rstrip()

# n 기타

n = int(input())

serial_list = []

# input
for i in range(n):
    count = 0
    serial_number = input()
    for i in serial_number:
        if i.isdigit():
            count += int(i)
    serial_list.append([serial_number, count])

serial_list.sort(key=lambda x: (len(x[0]), x[1], x[0]))
for x in serial_list:
    print(x[0])
