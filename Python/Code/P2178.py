# https://www.acmicpc.net/problem/2178

# graph = {
#     'A' : ['B','C'],
#     'B' : ['D', 'E'],
#     'C' : ['F'],
#     'D' : [],
#     'E' : ['F'],
#     'F' : []
# }
# 
# visited = [] # List to keep track of visited nodes.
# queue = []     #Initialize a queue
# 
# def bfs(visited, graph, node):
#     visited.append(node)
#     queue.append(node)
# 
#     while queue:
#         s = queue.pop(0)
#         print (s, end = " ")
# 
#         for neighbour in graph[s]:
#             if neighbour not in visited:
#                 visited.append(neighbour)
#                 queue.append(neighbour)


def bfs():
    while q:
        x, y = q.pop(0)
        for _ in range(4):
            dx, dy = d[_]
            nx = x + dx
            ny = y + dy
            # 범위 밖
            if nx < 0 or nx > M-1:
                continue
            if ny < 0 or ny > N-1:
                continue
            # 벽
            if maze_map[ny][nx] == 0:
                continue
            # 이미 방문
            if check[ny][nx] != 0:
                continue

            check[ny][nx] = check[y][x] + 1
            q.append([nx, ny])

    print(check[N-1][M-1])


# Driver Code
arr = []
N, M = map(int, input().split())
maze_map = [list(map(int, input())) for _ in range(N)]
q = [[0, 0]]
check = [[0] * M for _ in range(N)]
check[0][0] = 1
d = [[1, 0], [0, -1], [-1, 0], [0, 1]]
bfs()
