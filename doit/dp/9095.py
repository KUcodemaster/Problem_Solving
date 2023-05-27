n = int(input())

q = []

d = [0] * 11


for i in range(n):
    q.append(int(input()))

d[0] = 1
d[1] = 1
for i in range(2, 11):
    d[i] = d[i-1]
    if i >= 2:
        d[i] += d[i-2]
    if i >= 3:
        d[i] += d[i-3]

for i in q:
    print(d[i])