
#문제 https://www.acmicpc.net/problem/2588

#빠르게 해줌
import sys
input = lambda : sys.stdin.readline().rstrip()

#
three_digit_integer1 = int(input())
three_digit_integer2 = input()

place3 = three_digit_integer1 * int(three_digit_integer2[2])
place4 = three_digit_integer1 * int(three_digit_integer2[1])
place5 = three_digit_integer1 * int(three_digit_integer2[0])

place6 = place3 + place4 * 10 + place5 * 100

print(place3)
print(place4)
print(place5)
print(place6)
