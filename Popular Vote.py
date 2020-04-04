import sys

n, m = map(int, input().split())
a = list(map(int, input().split()))

sorted_a = sorted(a, reverse=True)

for i in range(m):
    if sorted_a[i] < sum(a) / 4 / m:
        print('No')
        sys.exit()
print('Yes')
