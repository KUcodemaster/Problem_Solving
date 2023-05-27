import sys
import heapq

input = sys.stdin.readline

q = []
n = int(input())

num = 0
for i in range(n):
    num = int(input())
    if num > 0:
        heapq.heappush(q, -num)
    else:
        if q:
            p = heapq.heappop(q)
            print(-p)
        else:
            print(0)