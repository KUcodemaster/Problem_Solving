n = int(input())

graph = []

for i in range(n):
    graph.append(list(map(int, input().split())))

blue = 0
white = 0

def find_color(g):
    large = -1
    small = 2
    for i in range(len(g)):
        large = max(max(g[i]), large)
        small = min(min(g[i]), small)

    if large == small:
        if large == 1:
            global blue
            blue += 1
            return True
        elif large == 0:
            global white
            white += 1
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
        for i in range(len(g)):
            if i < length // 2:
                s1.append(g[i][:length//2])
                s2.append(g[i][length//2:])
            else:
                s3.append(g[i][:length//2])
                s4.append(g[i][length//2:])
        q.append(s1)
        q.append(s2)
        q.append(s3)
        q.append(s4)

print(white)
print(blue)