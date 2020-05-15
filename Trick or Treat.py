n, k = map(int, input().split())
s = set()
for _ in range(k):
    d = int(input())
    s = s.union(list(map(int, input().split())))
print(n - len(s))
