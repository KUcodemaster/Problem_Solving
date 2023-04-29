n = int(input())

ans = []

for i in range(n):
    data = input().split()
    ans.append([data[0], int(data[1])])

ans.sort(key=lambda x: x[1])

for i in range(n):
    print(ans[i][0], end=' ')
print()