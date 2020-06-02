# https://www.acmicpc.net/problem/1712
# https://www.acmicpc.net/source/20156031

A, B, C = map(int, input().split())
F_cost = A
V_cost = B
P_revenue = C
S_digit = 10000000000
Count = 1

if P_revenue <= V_cost:
    print(-1)
    exit()

while True:
    if S_digit == 0 or F_cost == 0:
        print(Count)
        break
    temp_val = ((P_revenue - V_cost) * S_digit)
    if F_cost >= temp_val:
        Count += (F_cost // temp_val) * S_digit
        F_cost = F_cost % temp_val
    S_digit = S_digit // 10


