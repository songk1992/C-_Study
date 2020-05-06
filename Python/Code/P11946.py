
#문제 https://www.acmicpc.net/problem/11946
#참고 https://claude-u.tistory.com/347

#빠르게 해줌
import sys
input = lambda : sys.stdin.readline().rstrip()

# n teams
# m questions
# q score_log
n, m, q = map(int, input().split())

# [팀번호][문제번호][(301일때 못품, 301아닐때 걸린시간), 패널티시간]
A_list = [[[301, 0] for _ in range(m+1)] for _ in range(n+1)]



for _ in range(q):
    #입력
    time_passed, team_number, question_number, question_marking = (input().split())
    time_passed = int(time_passed)
    team_number = int(team_number)
    question_number = int(question_number)

    #체크후 A_list 채워줌
    if A_list[team_number][question_number][0] == 301:
        if question_marking == 'AC':
            A_list[team_number][question_number][0] = time_passed + A_list[team_number][question_number][1]
        else:
            A_list[team_number][question_number][1] += 20

#[팀번호][팀번호, 총푼문제수, 시간]
grade = [[i, 0, 0] for i in range(n+1)]

for team_number in range(1, n+1):
    for question_number in range(1, m+1):
        if A_list[team_number][question_number][0] != 301:
            grade[team_number][1] += 1
            grade[team_number][2] += A_list[team_number][question_number][0]

# sorting
grade.sort(key=lambda x:(-x[1], x[2], x[0]))
grade.remove([0,0,0])

# 출력
for x in grade:
    print(x[0], x[1], x[2])
