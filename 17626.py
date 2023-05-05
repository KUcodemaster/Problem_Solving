n = int(input())

d = [0] * 50001


for i in range(1, n+1):
    d[i] = d[i - 1] + 1
    for j in range(1,int(i**0.5)+1):
        d[i] = min(d[i-j**2] + 1, d[i])


print(d[n])