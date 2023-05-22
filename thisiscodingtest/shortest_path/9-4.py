INF = int(1e9)

n, m = map(int, input().split()) # 회사 수, 경로 수

graph = [[INF] * (n+1) for _ in range(n+1)]


for _ in range(m):
    a, b = map(int,input().split())
    graph[a][b] = 1
    graph[b][a] = 1

for i in range(n+1):
    for j in range(n+1):
        if i==j:
            graph[i][j] = 0

for k in range(n+1):
    for a in range(n+1):
        for b in range(n+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

x, k = map(int, input().split())

ans = graph[1][k] + graph[k][x]

if ans > 1000000:
    print(-1)
else:
    print(ans)