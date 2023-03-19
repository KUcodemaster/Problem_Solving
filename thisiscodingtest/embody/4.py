def get_next_dir(direction):
    if direction == 0:
        direction = 3
    else:
        direction -= 1
    return direction

def get_next_go(direction, row, col):
    if direction == 0:
        return (row - 1, col)
    elif direction == 1:
        return (row, col + 1)
    elif direction == 2:
        return (row + 1, col)
    else:
        return (row, col - 1)

def check_all_direction(row, col):
    if minimap[row - 1][col] and minimap[row + 1][col] and minimap[row][col + 1] and minimap[row][col - 1]:
        return 0
    else:
        return 1

def go_back(direction, row, col):
    if direction == 0:
        if minimap[row + 1][col]:
            return (-1, -1)
        else:
            return (row + 1, col)
    elif direction == 1:
        if minimap[row][col - 1]:
            return (-1, -1)
        else:
            return (row, col - 1)
    elif direction == 2:
        if minimap[row - 1][col]:
            return (-1, -1)
        else:
            return (row - 1, col)
    else:
        if minimap[row][col + 1]:
            return (-1, -1)
        else:
            return (row, col + 1)

n, m = map(int, input().split())

minimap = []
row, col, direction = map(int, input().split())
res = 0
for _ in range(n):
    minimap.append(list(map(int, input().split())))


while 1:
    next_direction = get_next_dir(direction) # 왼쪽 방향 회전
    next_row, next_col = get_next_go(next_direction, row, col) # 갈 row, col 정하기
    if not check_all_direction(row, col): # 갈 곳이 없을 때
        row, col = go_back(direction, row, col)
        minimap[row][col] = 1
        res += 1
        if row == -1 and col == -1:
            break
    elif minimap[next_row][next_col] == 0:
        minimap[next_row][next_col] = 1
        direction = next_direction
        row, col = next_row, next_col
        res += 1
    else:
        direction = next_direction
        continue
    

print(res)
