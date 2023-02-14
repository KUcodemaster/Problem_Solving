n = int(input())
arr = list(map(int, input().split()))

res = []
stack = [-1]

for i in range(n-1, -1, -1):
  while len(stack) > 1 and stack[-1] < arr[i]:
    stack.pop()
  res.append(stack[-1])
  stack.append(arr[i])

ans = " ".join(str(x) for x in res[::-1])
print(ans)