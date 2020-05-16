#https://www.acmicpc.net/problem/5597

total = 30
submit = 28

checkset = []
for student in range(total+1):
    checkset.append(student)
checkset = set(checkset)
#checkset = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30}

submit_set = [0] * total
for student in range(submit):
    submit_set[student] = int(input())
submit_set = set(sorted(submit_set))
#submit_set = {0, 1, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30}

not_been_submitted = sorted(checkset.difference(submit_set))

for student in not_been_submitted:
    print(student)
