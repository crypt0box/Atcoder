n = int(input())
p = list(map(int, input().split()))

cnt = 0
p_min = p[0]
for i in range(n):
    p_min = min(p_min, p[i])
    if p_min == p[i]:
        cnt += 1
print(cnt)
