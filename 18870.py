import sys

input = sys.stdin.readline

n = int(input())

num = list(map(int, input().split()))

nums = list(sorted(set(num)))

dic = {}

for i in range(len(nums)):
    dic[nums[i]] = i

for i in num:
    print(dic[i], end=' ')