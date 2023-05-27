from collections import deque 

n, m = map(int, input().split())

parent = [0] * (n+1)

edge = []

for i in range(len(parent)):
    parent[i] = i

for i in range(m):
    a, b, c = map(int, input().split())
    edge.append((c, a, b))

def find_parent(parent, a):
    if parent[a] != a:
        parent[a] = find_parent(parent, parent[a])
    return parent[a]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


edge.sort()

ans = 0
max_cost = 0

for e in edge:
    cost, a, b = e
  
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        max_cost = max(max_cost, cost)
        ans += cost


print(ans-max_cost)