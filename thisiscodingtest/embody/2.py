n = int(input())

h = 0
m = 0
s = 0

res = 0
for i in range(n+1):
    for j in range(60):
        for k in range(60):
            s += 1
            if '3' in str(h)+str(m)+str(s):
                res += 1
        s = 0
        m += 1
    m = 0
    h += 1
print(res)