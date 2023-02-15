#버블 정렬

n = int(input())

arr = []
for i in range(n):
	arr.append(int(input()))


for i in range(n-1):
	for j in range(i+1, n):
		if arr[i] > arr[j]:
			temp = arr[j]
			arr[j] = arr[i]
			arr[i] = temp

for i in arr:
	print(i)