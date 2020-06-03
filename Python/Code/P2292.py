# https://www.acmicpc.net/problem/2292

N = int(input())
number_of_rooms_to_travel = 1
number_of_rooms_that_exists = 1
while True:
    if N <= number_of_rooms_that_exists:
        print(number_of_rooms_to_travel)
        break
    number_of_rooms_that_exists += 6 * number_of_rooms_to_travel
    number_of_rooms_to_travel += 1

