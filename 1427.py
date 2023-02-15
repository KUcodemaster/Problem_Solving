n = list(input())
length = len(n)

for i in range(length):
	max = i
	for j in range(i, length):
		if n[j] > n[max]:
			max = j
	temp = n[i]
	n[i] = n[max]
	n[max] = temp
	
for i in n:
	print(i, end="")