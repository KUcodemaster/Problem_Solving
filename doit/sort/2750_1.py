#버블 정렬

n = int(input())

arr = []
for i in range(n):
	arr.append(int(input()))


for i in range(n-1):
	for j in range(n-i-1):
		if arr[j] > arr[j+1]:
			temp = arr[j+1]
			arr[j+1] = arr[j]
			arr[j] = temp

for i in arr:
	print(i)
