n = int(input())

arr = list(map(int,input().split()))

for i in range(1, n):
    to_insert = i
    from_insert = arr[i]
    for j in range(i-1,-1,-1):
        if arr[i] > arr[j]:
            to_insert = j+1
            break
        if j == 0:
            to_insert = 0
    for j in range(i, to_insert, -1):
        arr[j] = arr[j-1]
    arr[to_insert] = from_insert

sum_arr = [arr[0]]

for i in range(1, len(arr)):
    sum_arr.append(arr[i] + sum_arr[i-1])

print(sum(sum_arr))
