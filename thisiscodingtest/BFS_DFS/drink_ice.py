# BFS 알고리즘
from collections import deque

n, m = map(int, input().split())

graph = []
moves = [[0, 1], [1, 0], [0, -1], [-1, 0]]
visited = []

q = deque()
ans = []

for _ in range(n):
    line = list(input())
    graph.append(line)
    visited.append([0] * m)

# for i in range(n):
#     for j in range(m):
#         if graph[i][j] == '0' and visited[i][j] == 0:
#             ans += 1
#             print(i,j)
#             q.append(graph[i][j])
#             visited[i][j] = 1
#             while len(q) > 0:
#                 for move in moves:
#                     r = i + move[0]
#                     c = j + move[1]
#                     if r >= 0 and r < n and c >= 0 and c < m:
#                         if not visited[r][c]:
#                             q.append(graph[r][c])
#                             visited[r][c] = 1
                # q.popleft()

def dfs(i, j):
    if visited[i][j] == 1 or graph[i][j] == '1':
        return
    else:
        q.append((i, j))
        ans.append(1)
        while len(q) > 0:
            cur_r, cur_c = q.pop()
            for move in moves:
                r = cur_r + move[0]
                c = cur_c + move[1]
                if r >= 0 and r < n and c >= 0 and c < m:
                    if not visited[r][c] and graph[r][c] == '0':
                        q.append((r,c))
                        visited[r][c] = 1
                        dfs(r, c)


for i in range(n):
    for j in range(m):
        dfs(i, j)

print(len(ans))