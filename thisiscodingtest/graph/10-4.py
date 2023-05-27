from collections import deque
import copy

n = int(input())

cost = [0] * (n+1)
indegree = [0] *(n+1)
graph = [[] for _ in range(n+1)]

for i in range(1, n+1):
    data = list(map(int, input().split()))
    cost[i] = data[0]
    for x in data[1:-1]:
        indegree[i] += 1
        graph[x].append(i)

q = deque()

for i in range(n+1):
    if indegree[i] == 0:
        q.append(i)

ans = copy.deepcopy(cost)

while q:
    node = q.popleft()

    for i in graph[node]:
        ans[i] = max(ans[i], ans[node]+cost[i])
        indegree[i] -= 1
        if indegree[i] == 0:
            q.append(i)

for i in range(1, n+1):
    print(ans[i])