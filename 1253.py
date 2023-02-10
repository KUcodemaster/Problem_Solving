n = int(input())

arr = list(map(int, input().split()))

arr.sort()

ans = 0
for i in range(n-1, -1, -1):
    j, k = n - 1, 0
    tmp = arr[i]
    while j > k:
        if (arr[j] + arr[k] > tmp):
            j -= 1
            if i == j:
                j -= 1
        elif (arr[j] + arr[k] < tmp):
            k += 1
            if i == k:
                k += 1
        else:
            if i == k:
                k += 1
            elif i == j:
                j -= 1
            else:
                print(arr[j], arr[k], tmp)
                ans += 1
                break

print(ans)