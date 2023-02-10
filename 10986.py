import sys
input = sys.stdin.readline

n, m = map(int, input().split())

arr = list(map(int, input().split()))
cnt = [0] * m
sum_arr = [arr[0]]

ans = 0
for i in range(1, len(arr)):
    sum_arr.append(sum_arr[i-1] + arr[i])
for i in range(n):
    tmp = sum_arr[i] % m
    if tmp == 0:
      ans += 1
    cnt[tmp] += 1

for i in range(m):
  if cnt[i] > 1:
     ans += (cnt[i] * (cnt[i] - 1) // 2)

print(ans)