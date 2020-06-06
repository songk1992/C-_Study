# https://www.acmicpc.net/problem/11729


arr = [[1], [1, 1]]
max_n = 30

for i in range(1, max_n-1):
    temp_list = [1]
    for j in range(len(arr[i])-1):
        temp_list.append(arr[i][j] + arr[i][j + 1])
    temp_list.append(1)
    arr.append(temp_list)


n, k = map(int, input().split())
print(arr[n-1][k-1])
