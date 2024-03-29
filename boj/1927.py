import sys
import heapq

input = sys.stdin.readline

n = int(input())

q = []
for i in range(n):
    ins = int(input())
    if ins == 0:
        if len(q) == 0:
            print(0)
        else:
            print(heapq.heappop(q))
    else:
        heapq.heappush(q,ins)