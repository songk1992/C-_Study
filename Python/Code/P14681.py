#python 3.7.1

#https://www.acmicpc.net/problem/14681


def f(c1, c2):
  q = 0
  if x > 0 and y > 0:
    q = 1
    
  if x < 0 and y > 0:
    q = 2
  
  if x < 0 and y < 0:
    q = 3
  
  if x > 0 and y < 0:
    q = 4
  return q

x = int(input())
y = int(input())

print(f(x, y))
