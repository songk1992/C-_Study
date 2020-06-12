# https://www.acmicpc.net/problem/2606
def bfs(q):
    cnt = 0
    while q:
        k = q.pop(0)
        for _ in range(len(Edges[k-1])):
            if Edges[k-1][_] not in visited:
                q.append(Edges[k-1][_])
                visited.append(Edges[k-1][_])
                cnt += 1
    print(cnt)


number_of_computers = int(input())
number_of_edges = int(input())
Edges = [[0] * (number_of_computers) for _ in range(number_of_computers)]

q = [1]
visited = [0, 1]
for _ in range(number_of_edges):
    n1, n2 = map(int, input().split())
    Edges[n1-1][n2-1] = n2
    Edges[n2-1][n1-1] = n1

bfs(q)
