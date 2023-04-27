from collections import deque

n, m = map(int,input().split())
graph = []
visited = [[0] * m for _ in range(n)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


for _ in range(n):
    graph.append(list(map(int, input())))

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = 1

    while len(queue) > 0:
        x, y = queue.popleft()

        for i in range(4):
            cur_x = x + dx[i]
            cur_y = y + dy[i]
            if cur_x < 0 or cur_y < 0 or cur_x >= n or cur_y >= m:
                continue
            if graph[cur_x][cur_y] == 1 and not visited[cur_x][cur_y]:
                queue.append((cur_x, cur_y))
                visited[cur_x][cur_y] = 1
                graph[cur_x][cur_y] += graph[x][y]
                if cur_x == n-1 and cur_y == m-1:
                    return graph[cur_x][cur_y]

print(bfs(0, 0))