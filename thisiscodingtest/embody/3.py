current = input()

col = "abcdefgh"

cur_col = col.find(current[0])
cur_row = int(current[1]) - 1

move_col = [2, 2, -2, -2, 1, 1, -1, -1]
move_row = [1, -1, 1, -1, 2, -2, 2, -2]

res = 0
for i in range(8):
    if cur_row + move_row[i] < 0 or cur_row + move_row[i] > 7:
        continue
    elif cur_col + move_col[i] < 0 or cur_col + move_col[i] > 7:
        continue
    else:
        res += 1

print(res)
