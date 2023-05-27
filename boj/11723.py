import sys

input = sys.stdin.readline

m = int(input())

d = {}

for i in range(m):
    inst = input().split()

    if inst[0] == 'add':
        d[int(inst[1])] = 1
    elif inst[0] == 'remove':
        if int(inst[1]) in d:
            d.pop(int(inst[1]))
    elif inst[0] == 'check':
        if int(inst[1]) in d:
            print(1)
        else:
            print(0)
    elif inst[0] == 'toggle':
        if int(inst[1]) in d:
            d.pop(int(inst[1]))
        else:
            d[int(inst[1])] = 1
    elif inst[0] == 'all':
        for i in range(1, 21):
            d[i] = 1
    elif inst[0] == 'empty':
        d.clear()
        