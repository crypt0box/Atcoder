n, x = map(int, input().split())
a = list(map(int, input().split()))
a_asc = sorted(a)
ans = 0
for i in range(n):
    x -= a_asc[i]
    if x >= 0:
        ans += 1
print(ans - 1 if x != 0 and x > 0 else ans)
# 要復習
