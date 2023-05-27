import sys

input = sys.stdin.readline

n = int(input())

nums = []

def avg(nums):
    temp = 0
    for i in range(len(nums)):
        temp += nums[i]
    res = temp / len(nums)
    return round(res)

def mid(nums):
    nums.sort()
    return nums[len(nums)//2]

def mode(nums):
    num = [0] * 8002
    for i in range(len(nums)):
        num[nums[i]+4000] += 1

    temp_mode = max(num)

    ans = []
    for i in range(len(num)):
        if num[i] == temp_mode:
            ans.append(i-4000)
    if len(ans) > 1:
        return ans[1]
    else:
        return ans[0]


for i in range(n):
    nums.append(int(input()))
    
print(avg(nums))
print(mid(nums))
print(mode(nums))
print(max(nums)-min(nums))

    