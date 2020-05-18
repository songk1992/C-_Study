#python 3.7.1

#https://www.acmicpc.net/problem/10179


T = int(input())

for _ in range(T):
    amount = round(0.8*float(input()), 2)
    amount = str(amount)
    if (amount[-3:-2] == "."):
        print('${}'.format(amount))
    else:
        print('${}0'.format(amount))
