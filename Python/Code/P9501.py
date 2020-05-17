#python 3.7.1

#https://www.acmicpc.net/problem/9501



#Test case T
T = int(input())

number_of_successful_ships_per_testcase = []


for _ in range(T):

    # reset count
    count = 0

    # N number of rockets
    # D distance
    N, D = map(int, input().split())

    for _ in range(N):

        # v average velocity
        # f fuel capacity
        # c fuel efficiency
        v, f, c = map(float, input().split())
        if((v * f/c) >= D):
            count += 1

    number_of_successful_ships_per_testcase.append(count)

for successful_ships_in_testcase in number_of_successful_ships_per_testcase:
    print(successful_ships_in_testcase)
