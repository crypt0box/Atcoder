n, k = map(int, input().split())
h = list(map(int, input().split()))

h = sorted(h, reverse=True)

del h[:k]

print(sum(h) if h != 0 else 0)
