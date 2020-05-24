#python 3.7.1

#https://www.acmicpc.net/problem/2884


def f(time, minute):
  if minute >= 45:
    minute -= 45
  else:
    minute += 15
    time -= 1
    if time < 0:
      time = 23
  print("{} {}".format(time, minute))
  

time, minute = map(int, input().split())

f(time, minute)
