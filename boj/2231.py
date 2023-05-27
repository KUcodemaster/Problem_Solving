n = int(input())
find = 0
for i in range(1, 1000001):
    const = i

    tmp = str(i)
    for j in range(len(tmp)):
        const += int(tmp[j])
    if const == n:
        print(i)
        find = 1
        break
if not find:
    print(0)