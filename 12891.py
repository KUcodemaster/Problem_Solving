import sys

input = sys.stdin.readline

s, p = map(int, input().split())

string = list(input())
condition = list(map(int, input().split()))

ans = 0
frequency = [0] * 4

part = string[:p]
for el in part: # 최초 값 계산
	if el == 'A':
		frequency[0] += 1
	elif el == 'C':
		frequency[1] += 1
	elif el == 'G':
		frequency[2] += 1
	else:
		frequency[3] += 1

if frequency[0] >= condition[0] and frequency[1] >= condition[1] and frequency[2] >= condition[2] and frequency[3] >= condition[3]:
		ans += 1

for i in range(1, s-p+1): # 빠지는 부분, 추가되는 부분 계산
	left = i - 1
	if string[left] == 'A':
		frequency[0] -= 1
	elif string[left] == 'C':
		frequency[1] -= 1
	elif string[left] == 'G':
		frequency[2] -= 1
	else:
		frequency[3] -= 1
	
	new = i+p-1
	if string[new] == 'A':
		frequency[0] += 1
	elif string[new] == 'C':
		frequency[1] += 1
	elif string[new] == 'G':
		frequency[2] += 1
	else:
		frequency[3] += 1
	if frequency[0] >= condition[0] and frequency[1] >= condition[1] and frequency[2] >= condition[2] and frequency[3] >= condition[3]:
		ans += 1


print(ans)