import sys
import heapq

n = int(input().strip())

input = sys.stdin.readline

for i in range(n):
    k = int(input().strip())
    visit = [0] * 1000001
    if k == 0:
        continue
    l = 0
    m = 0
    q = []
    q2 = []
    for j in range(k):
        a = input().strip().split()

        if a[0] == "I":
            heapq.heappush(q, (int(a[1]), j)) 
            heapq.heappush(q2, (-int(a[1]), j))
            visit[j] = 1
        elif a[0] == "D":
            if a[1] == '-1':
                while q and not visit[q[0][1]]:
                    heapq.heappop(q)
                if q:
                    visit[q[0][1]] = 0
                    heapq.heappop(q)
            elif a[1] == '1':
                while q2 and not visit[q2[0][1]]:
                    heapq.heappop(q2)
                if q2:
                    visit[q2[0][1]] = 0
                    heapq.heappop(q2)
                    
    while q and not visit[q[0][1]]:
        heapq.heappop(q)
    while q2 and not visit[q2[0][1]]:
        heapq.heappop(q2)

    z, x = None, None # 최소 최대
    if q:
        z = heapq.heappop(q)[0]
    if q2:
        x = -heapq.heappop(q2)[0]
    if z == None and x == None :
        print('EMPTY')
    else:
        print(x, z)
