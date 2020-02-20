n = int(input())
a = list(map(int, input().split()))
a_desc = sorted(a, reverse=True)
del a_desc[:n]
ans = 0
for i in range(n):
    ans += a_desc[i]
print(a_desc)