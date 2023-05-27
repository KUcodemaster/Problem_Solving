channel = int(input())

m = int(input())
num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

if m != 0:
    broken = list(map(int,input().split()))
    for i in broken:
        num.remove(i)


ch = set()

# num에서 1개 선택, 2개 선택 ... 6개 선택 모든 경우

def dfs(depth, current_depth, channel):
    if depth == current_depth or (current_depth == 5 and channel // 100000 >= 5):
        return
    else:
        for n in num:
            n = channel * 10 + n
            ch.add(n)
            dfs(depth, current_depth+1, n)

dfs(6, 0, 0)



def plus_minus_to_go(num, fr):
    return abs(num - fr)

res = 999999
cnt = 0
if ch:
    for c in ch:
        res = min(res, plus_minus_to_go(channel, 100), plus_minus_to_go(channel, c) + len(str(c)))
else:
    res = plus_minus_to_go(channel, 100)

print(res)
