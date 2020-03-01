n, m = map(int, input().split())

l = [list(map(int, input().split())) for _ in range(m)]
l = sum(l, [])

for i in range(1, n + 1):
    x = 0
    for j in range(len(l)):
        if i == l[j]:
            x += 1
    print(x)