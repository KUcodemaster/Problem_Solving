from collections import deque

N, L = map(int,input().split())
mydeque = deque()
arr = list(map(int,input().split()))

for i in range(N): # 덱에 (숫자, 인덱스) 튜플로 저장
	while mydeque and mydeque[-1][0] >= arr[i]: # 큰 값 제거
		mydeque.pop()
	mydeque.append((arr[i], i))
	if mydeque[0][1] <= i - L: # 범위 지난 값 제거
		mydeque.popleft()
	print(mydeque[0][0], end=" ")