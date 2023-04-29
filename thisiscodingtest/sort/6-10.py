n = int(input())

ans = [0] * 100001
for i in range(n):
    ans[int(input())] += 1

for i in range(100000, -1, -1):
    while ans[i] > 0:
        print(i, end=' ')
        ans[i] -= 1
print()