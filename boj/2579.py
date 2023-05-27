import sys

input = sys.stdin.readline

n = int(input())

st = [0] * 301
dp = [0] * 301
for i in range(n):
    st[i] = int(input())


if n > 3:
  dp[0] = st[0]
  dp[1] = st[0]+st[1]
  dp[2] = max(st[0]+st[2], st[1]+st[2])
  for i in range(3, n):
      dp[i] = max(dp[i-2]+st[i], dp[i-3]+st[i-1]+st[i])
    

if n == 1:
    print(st[0])
elif n == 2:
    print(st[0]+st[1])
elif n == 3:
    print(max(st[0]+st[2], st[1]+st[2]))
else:
    print(dp[n-1])
