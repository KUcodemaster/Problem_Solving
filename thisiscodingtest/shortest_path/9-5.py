import heapq

n,m,c = map(int,input().split()) # 노드, 간선, 시작점

INF = int(1e9)
graph = [[] for i in range(n+1)]
costs = [INF] * (n+1)


for i in range(m):
    x,y,z = map(int, input().split())
    graph[x].append((y, z))

q = []

heapq.heappush(q, (0, c))
costs[c] = 0

while q:
    cost, start = heapq.heappop(q)

    if costs[start] < cost:
        continue
    
    for i in graph[start]:
        dist = cost + i[1]
        if dist < costs[i[0]]:
            costs[i[0]] = dist
            heapq.heappush(q, (dist, i[0]))

cnt = 0
max_distance = 0

for i in costs:
    if i != INF:
        cnt += 1
        max_distance = max(max_distance, i)

print(cnt-1, max_distance)