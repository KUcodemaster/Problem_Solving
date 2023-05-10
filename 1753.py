import heapq
import sys

input = sys.stdin.readline

v, e = map(int, input().split())
start = int(input())


graph = [[] for i in range(v+1)]
visited = [0] * (v+1)

ans = [987654321] * (v+1)

q = []
for i in range(e):
    a, b, c = map(int, input().split()) # from, to, cost
    graph[a].append((c, b)) # cost, to

heapq.heappush(q, (0, start))
ans[start] = 0

while q:
    cost, now = heapq.heappop(q)
    if visited[now] == 1:
        continue
    if ans[now] > cost:
        ans[now] = cost
    
    visited[now] = 1
    
    for edge in graph[now]:
        edge_cost, edge_now = edge
        heapq.heappush(q, (edge_cost + cost, edge_now))

for i in range(1, len(ans)):
    if ans[i] == 987654321:
        print('INF')
    else: 
        print(ans[i])
