a, b, k = map(int, input().split())

total = a + b - k

if a >= k:
    print(a-k, b)
elif a < k <= a + b:
    print(0, b - (k - a))
else:
    print(0, 0)
