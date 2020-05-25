# https://www.acmicpc.net/problem/11723
import sys

input = lambda: sys.stdin.readline().rstrip()


def operator(op, number):
    number = int(number)
    temp_set = {number}

    if op == 'add':
        S.add(number)
    if op == 'remove':
        if S.intersection(temp_set):
            S.remove(number)
    if op == 'check':
        if S.intersection(temp_set):
            print(1)
        else:
            print(0)
    if op == 'toggle':
        if S.intersection(temp_set):
            S.remove(number)
        else:
            S.add(number)


S = set()
S_all_tuple = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20}
S_all = set(S_all_tuple)

n = int(input())

for _ in range(n):
    what_you_type = input().split(' ')
    if what_you_type == ['empty']:
        S.clear()
    elif what_you_type == ['all']:
        S = S.union(S_all)
    else:
        n1, n2 = [j for j in what_you_type]
        operator(n1, n2)
