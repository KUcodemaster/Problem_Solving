n = int(input())
data = list(map(int, input().split()))
m = int(input())
req = list(map(int, input().split()))

data.sort()

def binary_search(data, to_find, start, end):
    while start <= end:
        mid = (start+end) // 2
        if data[mid] == to_find:
            return True
        elif data[mid] > to_find:
            end = mid - 1
        else:
            start = mid + 1
    return False

for i in range(m):
    if not binary_search(data, req[i], 0, n-1):
        print('no', end=' ')
    else:
        print('yes', end=' ')
print()


