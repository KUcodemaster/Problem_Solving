import sys
input = sys.stdin.readline

data, num = map(int, input().split())
arr = list(map(int,input().split()))
sum_arr = []

for i in range(len(arr)):
    if len(sum_arr) == 0:
        sum_arr.append(arr[i])
    else:
        sum_arr.append(sum_arr[i - 1] + arr[i])
        
for _ in range(num):
    a, b = map(int, input().split())
    if a == 1:
        print(sum_arr[b - 1])
    else:
        print(sum_arr[b - 1] - sum_arr[a - 2])
