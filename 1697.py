from collections import deque

q = deque()

n, k = map(int, input().split())



q.append((n, 0))

visited = [0] * 100001

while q:
    num, cnt = q.popleft()
    if num == k:
        print(cnt)
        break

    
    if num - 1 >= 0 and not visited[num-1]:
      q.append((num - 1, cnt+1))
      visited[num-1] = 1
    if num + 1 <= 100000 and not visited[num+1]:
      q.append((num + 1, cnt+1))
      visited[num+1] = 1
    if num * 2 <= 100000 and not visited[num*2]:
      q.append((num * 2, cnt+1))
      visited[num*2] = 1


