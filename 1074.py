n, r, c = map(int, input().split())

ans = 0

r += 1
c += 1
while n != 0:
    total_r = 2 ** n
    total_c = 2 ** n

    if r <= total_r // 2 and c <= total_c // 2:
        ans += 0
    elif r >= total_r // 2 and c <= total_c // 2:
        ans += 4 ** n // 2
        r = r - total_r // 2
    elif r <= total_r // 2 and c >= total_c // 2:
        ans += 4 ** n // 4
        c = c - total_c // 2
    elif r >= total_r // 2 and c >= total_c // 2:
        ans += 4 ** n // 2 + 4 ** n // 4
        r = r - total_r // 2
        c = c - total_c // 2
    
    # print(ans, r, c, total_r, total_c)
    n -= 1


print(ans)