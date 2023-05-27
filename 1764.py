import sys

input = sys.stdin.readline

n, m = map(int, input().strip().split())

dic = {}

for i in range(n):
    a = input().strip()
    dic[a] = a

res = []
for j in range(m):
    a = input().strip()
    if a in dic:
        res.append(a)

res.sort()

print(len(res))
for i in res:
    print(i)
