n, m = map(int, input().split())

d = [-1] * 10001

money = []

for i in range(n):
    tmp = int(input())
    money.append(tmp)
    d[tmp] = 1

for i in range(1, m+1):
    for j in money:
        if i - j >= 1:
            if d[i] == -1:
                d[i] = d[i-j] + 1
            elif d[i-j] != -1:
                    d[i] = min(d[i-j] + 1, d[i])


print(d[m])
