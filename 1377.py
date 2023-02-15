#버블 정렬

n = int(input())

arr = []
for i in range(n):
	arr.append(int(input()))


for i in range(n):
	changed = False
	for j in range(0, n-i-1):
		if arr[j] > arr[j+1]:
			changed = True
			temp = arr[j]
			arr[j] = arr[j+1]
			arr[j+1] = temp
	if changed == False:
		print(i+1)
		break
