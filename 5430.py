import sys 

input = sys.stdin.readline

n = int(input())


for i in range(n):
    flag = False
    instruction = list(input().strip())
    a = input()
    arr = input().strip().split(',')
    
    if len(arr):
        arr[0] = arr[0][1:]
    if len(arr) >= 1:
        arr[-1] = arr[-1][:-1]
    
    if arr[0] == '':
        arr = []
    
    direction = False # True = 역방향
    d = 0
    l = 0
    r = len(arr)-1

    for j in instruction:
        if j == 'R':
            direction = not direction
        if j == 'D':
            if not direction:
                l += 1
            else:
                r -= 1
            if l > len(arr) or r < -1 or l > r+1:
                print('error')
                flag=True
                break

    if not flag:
        arr = arr[l:r+1]
        
        if not direction:
            print('[', end='')
            for k in range(len(arr)):
                if k == len(arr)-1:
                    print(arr[k], end='')
                else:
                    print(arr[k], end=',')
            print(']', end='')
            print()
        else:
            print('[', end='')
            for k in range(len(arr)-1, -1, -1):
                if k == 0:
                    print(arr[k], end='')
                else:
                    print(arr[k], end=',')
            print(']', end='')
            print()
                
