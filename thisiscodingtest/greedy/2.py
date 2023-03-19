r, c = map(int, input().split())

cards = []

for i in range(r):
    cards.append(list(map(int, input().split())))

res = []
for row in cards:
    res.append(min(row))

print(max(res))