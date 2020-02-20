n, k = map(int, input().split())
l = list(map(int, input().split()))
l_asc = sorted(l, reverse=True)
ans = 0
for i in range(k):
    ans += l_asc[i]
print(ans)
