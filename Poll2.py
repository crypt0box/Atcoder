import collections

n = int(input())
s = [str(input()) for _ in range(n)]
ans = []

c = collections.Counter(s)

m = max(c.values()) # ここでmaxを代入しないとfor毎にmaxを計算することになり遅くなってTLE
for i in c:
    if c[i] == m:
        ans.append(i)
ans.sort()

for i in ans:
    print(i)
