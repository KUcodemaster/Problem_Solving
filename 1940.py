n = int(input())
m = int(input())

arr = list(map(int, input().split()))

arr.sort()

ans = 0

i = 0
j = len(arr) - 1

while i != j:
    if arr[i] + arr[j] > m:
        j -= 1
    elif arr[i] + arr[j] < m:
        i += 1
    else:
        j -= 1
        ans += 1

print(ans)