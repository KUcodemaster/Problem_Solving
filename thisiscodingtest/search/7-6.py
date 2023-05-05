n, m = map(int,input().split())

data = list(map(int, input().split()))

data.sort()

# 이진 탐색을 위한 시작점과 끝점 설정
len_max = data[-1]
len_min = 0

res = 0
while len_min <= len_max:
    mid = (len_min+len_max) // 2
    ans = 0

    for i in range(n):
        if data[i] > mid:
            ans += data[i] - mid
    
    if ans >= m:
        res = mid
        len_min = mid + 1
    else:
        len_max = mid - 1
print(res)