from collections import deque
import sys

input = sys.stdin.readline

n, m = map(int,input().split())

people = [0] * n
edge = [[] for _ in range(n)]
answer = 0

stack = deque()

for _ in range(m):
    i, j = map(int,input().split())
    edge[i].append(j)
    edge[j].append(i)

def dfs(lv):
  if lv == 4:
    global answer
    answer = 1
    return
  if len(stack) > 0:
      current = stack.pop()
      for i in edge[current]:
        if visited[i] == 0:
          visited[i] += 1
          stack.append(i)
          dfs(lv+1)
      visited[current] = 0

for start in range(n):
  stack.clear()
  visited = [0] * n
  visited[start] = 1
  stack.append(start)
  dfs(0)
  if answer == 1:
    break

if answer == 1:
  print(1)
else:
  print(0)
