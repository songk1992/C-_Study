# https://www.acmicpc.net/problem/1018

BC = [['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
      ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
      ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
      ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
      ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
      ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
      ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
      ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W']]

WC = [['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
      ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
      ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
      ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
      ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
      ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
      ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
      ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B']]

N, M = map(int, input().split())
arr = [list(input()) for i in range(N)]

#
q = []
for i in range(N-7):
    for j in range(M-7):
        q.append([i, j])


#
cnt = 64
while q:
    n1, n2 = q.pop(0)
    cntB = 0
    cntW = 0
    for i in range(8):
        for j in range(8):
            if arr[i+n1][j+n2] != BC[i][j]:
                cntB += 1

            if arr[i+n1][j+n2] != WC[i][j]:
                cntW += 1
    cnt = min(cntW, cntB, cnt)
print(cnt)
