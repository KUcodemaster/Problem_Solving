from collections import deque

num = int(input())

arr = deque([x for x in range(1, num+1)])

while len(arr) > 1:
    arr.popleft()
    arr.append(arr.popleft())

print(arr[0])