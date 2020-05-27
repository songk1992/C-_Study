# https://www.acmicpc.net/problem/5585
def f(arg, c):
    if arg >= 500:
        c += 1
        arg -= 500
    elif 100 <= arg < 500:
        c += 1
        arg -= 100
    elif 50 <= arg < 100:
        c += 1
        arg -= 50
    elif 10 <= arg < 50:
        c += 1
        arg -= 10
    elif 5 <= arg < 10:
        c += 1
        arg -= 5
    elif 1 <= arg < 5:
        c += 1
        arg -= 1
    return arg, c


change = 1000 - int(input())
count = 0
while True:
    change, count = f(change, count)
    if change == 0:
        print(count)
        break
