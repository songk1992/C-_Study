


#https://www.acmicpc.net/problem/1065
#http://kongming.net/11/i/p/?p=302-Han-Sui

import math

N = (input())
Counter = 0
checklist = list()

while True:

    DigitsArray = [int(steps) for steps in str(N)]

    DigitsArray = [int(steps) for steps in DigitsArray]

    length = len(DigitsArray)
    if length == 1:
        Counter += 1

    elif length == 2:
        Counter += 1

    elif length > 2:
        checklist = [DigitsArray[i+1] - DigitsArray[i] for i in range(len(DigitsArray)-1)]

    checker = False
    if len(checklist) > 0:
        checker = all(elem == checklist[0] for elem in checklist)
    if checker:
        Counter +=1


    int_N = int(N)
    int_N -= 1
    N = int_N

    if N == 0:
        break
print(Counter)
