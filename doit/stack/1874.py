import sys

input = sys.stdin.readline

n = int(input())

stack_num = 0
stack = []
num = []
ans = []

for i in range(n):
	num.insert(0, int(input()))

while num:
	if num[-1] > stack_num:
		stack_num += 1
		stack.append(stack_num)
		ans.append("+")
	elif num[-1] <= stack[-1] and len(stack) > 0:
		stack.pop()
		num.pop()
		ans.append("-")
	else:
		print("NO")
		print(ans)
		ans = []
		break

for _ in ans:
	print(_)