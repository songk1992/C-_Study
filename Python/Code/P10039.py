# https://www.acmicpc.net/problem/10039
Number_of_Students = 5
Student_list = []
for _ in range(Number_of_Students):
    temp_value = int(input())
    if temp_value < 40:
        temp_value = 40
    Student_list.append(temp_value)

Average = sum(Student_list)//Number_of_Students
print(Average)
