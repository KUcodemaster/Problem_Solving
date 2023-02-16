import sys

input = sys.stdin.readline

arr = [0] * 10001

n = int(input())

for i in range(n):
    tmp = int(input())
    arr[tmp] += 1

for i in range(len(arr)):
    while arr[i] != 0:
        print(i)
        arr[i] -= 1