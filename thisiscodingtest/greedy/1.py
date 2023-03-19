n, m, k = map(int, input().split())

nums = list(map(int, input().split()))

nums.sort(reverse=True)

res = 0
repeat = k
while m:
    if repeat > 0:
        res += nums[0]
        repeat -= 1
    else:
        res += nums[1]
        repeat = k
    m -= 1
print(res)