from collections import deque

n = int(input())

def find_max(q):
    res = -1
    for i in range(len(q)):
        res = max(res, q[i][0])
    return res

for i in range(n):
    n, m = map(int, input().split())
    weight = list(map(int, input().split()))
    q = deque()
    for j in range(len(weight)):
        q.append((weight[j], j))

    num = 0
    while q:
        if q[0][0] == find_max(q):
            num += 1
            tmp = q.popleft()
            if tmp[1] == m:
                break
        else:
            tmp = q.popleft()
            q.append(tmp)
    print(num)