#python 3.7.1

#https://www.acmicpc.net/problem/6996


T = int(input())

for _ in range(T):
    compared_string1, compared_string2 = input().split()
    if sorted(compared_string1) == sorted(compared_string2):
        print("{} & {} are anagrams.".format(compared_string1, compared_string2))
    else:
        print("{} & {} are NOT anagrams.".format(compared_string1, compared_string2))
