n = int(input())

x, y = 1, 1
move = list(input().split())

for go in move:
    if go == 'R':
        if x == n:
            continue
        else:
            x += 1
    elif go == 'L':
        if x == 1:
            continue
        else:
            x -= 1
    elif go == 'U':
        if y == 1:
            continue
        else:
            y -= 1
    elif go == 'D':
        if y == n:
            continue
        else:
            y += 1
print(y, x)
