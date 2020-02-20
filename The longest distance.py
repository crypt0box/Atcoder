n = int(input())
e = [[int(i) for i in input().split()] for i in range(n)]
ans = 0
for i in range(n):
    for j in range(n):
        d = ((e[i][0] - e[j][0])**2 + (e[i][1] - e[j][1])**2)**0.5
        if d > ans:
            ans = d
print(ans)