#   https://www.acmicpc.net/problem/1260
#   BFS DFS 참조(1) https://m.blog.naver.com/wpghks7/221602789884
#   BFS DFS 참조(2) https://itholic.github.io/python-bfs-dfs/
#   BFS DFS 참조(3) https://cyc1am3n.github.io/2019/04/26/bfs_dfs_with_python.html

from collections import deque

def DFS(graph, root):
    visited = []
    stack = [root]

    while stack:
        n = stack.pop()
        if n not in visited:
            visited.append(n)
            if n in graph:
                temp = list(set(graph[n]) - set(visited))
                temp.sort(reverse = True)
                stack += temp
    return " ".join(str(i) for i in visited)

def BFS(graph, root):
    visited = []
    queue = deque([root])

    while queue:
        n = queue.popleft()
        if n not in visited:
            visited.append(n)
            if n in graph:
                temp = list(set(graph[n]) - set(visited))
                temp.sort()
                queue += temp
    return " ".join(str(i) for i in visited)

graph = {}
n = input().split(' ')
node, edge, start = [int(i) for i in n]
for i in range(edge):
    edge_info = input().split(' ')
    n1, n2 = [int(j) for j in edge_info]

    if n1 not in graph:
        graph[n1] = [n2]
    elif n2 not in graph[n1]:
        graph[n1].append(n2)

    if n2 not in graph:
        graph[n2] = [n1]
    elif n1 not in graph[n2]:
        graph[n2].append(n1)

print(DFS(graph, start))
print(BFS(graph, start))


# # 입력
# import queue
#
# number_of_nodes, number_of_edges, start_node = map(int, input().split())  # 정점의 개수, 간선의 개수, 시작 번호
#
# list_of_edges = [list() for _ in range(number_of_nodes + 1)]
# for _ in range(number_of_edges):
#     x, y = map(int, input().split())
#     list_of_edges[x].append(y)
#     list_of_edges[y].append(x)
# for x in list_of_edges:
#     x.sort()
#
# # BFS
#
# def bfs(bfs_start_node):
#     q = queue.Queue()
#     q.put(bfs_start_node)
#     check_list[bfs_start_node] = True
#
#     while not q.empty():
#         current_node = q.get()
#         print(current_node, end=" ")
#         for next_node in list_of_edges[current_node]:
#             if not check_list[next_node]:
#                 check_list[next_node] = True
#                 q.put(next_node)
#     print()
#
#
# # DFS
#
# def dfs(dfs_start_node):
#     stack = [dfs_start_node]
#
#     while stack:
#         current_node = stack.pop()
#         if check_list[current_node] == False:
#             print(current_node, end = " ")
#             check_list[current_node] = True
#             for x in list_of_edges[current_node]:
#                 if check_list[x] == False:
#                     stack.append(x)
#
#
# # main
# check_list = [False] * (number_of_nodes + 1)
# dfs(start_node)
#
# print()
#
# check_list = [False] * (number_of_nodes + 1)
# bfs(start_node)
