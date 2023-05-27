import sys

input = sys.stdin.readline

n = int(input())

graph = []

for i in range(n):
    graph.append(list(map(int, input().split())))

minus_one = 0
zero = 0
plus_one = 0

def find_color(g):
    large = -2
    small = 2
    for i in range(len(g)):
        large = max(max(g[i]), large)
        small = min(min(g[i]), small)

        if large != small:
            return False

    if large == small:
        if large == 1:
            global plus_one
            plus_one += 1
            return True
        elif large == 0:
            global zero
            zero += 1
            return True
        elif large == -1:
            global minus_one
            minus_one += 1
            return True
    else:
        return False

q = []

q.append(graph)

while q:
    g = q.pop()
    length = len(g)

    if not find_color(g):
        s1 = []
        s2 = []
        s3 = []
        s4 = []
        s5 = []
        s6 = []
        s7 = []
        s8 = []
        s9 = []
        for i in range(len(g)):
            if i < length // 3:
                s1.append(g[i][:length//3])
                s2.append(g[i][length//3:(length//3)*2])
                s3.append(g[i][(length//3)*2:])
            elif i < (length // 3)*2:
                s4.append(g[i][:length//3])
                s5.append(g[i][length//3:(length//3)*2])
                s6.append(g[i][(length//3)*2:])
            else:
                s7.append(g[i][:length//3])
                s8.append(g[i][length//3:(length//3)*2])
                s9.append(g[i][(length//3)*2:])
        q.append(s1)
        q.append(s2)
        q.append(s3)
        q.append(s4)
        q.append(s5)
        q.append(s6)
        q.append(s7)
        q.append(s8)
        q.append(s9)


print(minus_one)
print(zero)
print(plus_one)