n, k = map(int, input().split())

mod = n%k
if mod < k:
    print(min(abs(mod-k),mod))
else:
    print(mod)