#python 3.7.1

#https://www.acmicpc.net/problem/5565


TotalPrice = int(input())
BookPrice = TotalPrice

for _ in range(9):
    BookPrice = BookPrice - int(input())

print(BookPrice)
