# https://www.acmicpc.net/problem/12790
# 인상깊은 코드 https://www.acmicpc.net/source/17992954

def corrector1(arg):
    if arg < 1:
        arg = 1
    return arg


def corrector2(arg):
    if arg < 0:
        arg = 0
    return arg


def combat_power(arg):
    HP, MP, AP, DP, item_HP, item_MP, item_AP, item_DP = arg

    HP = HP + item_HP
    MP = MP + item_MP
    AP = AP + item_AP
    DP = DP + item_DP

    HP = corrector1(HP)
    MP = corrector1(MP)
    AP = corrector2(AP)

    combat_power_value = HP + (MP * 5) + (AP * 2) + (DP * 2)

    return combat_power_value


T = int(input())

for _ in range(T):
    character_info = map(int, input().split(' '))
    print(combat_power(character_info))
