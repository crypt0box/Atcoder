import math

a, b = map(int, input().split())
ans = float('inf')

for i in range(1, 1001):
    if math.floor(i * 0.08) == a and math.floor(i * 0.1) == b:
        if ans > i:
            ans = i

if ans == float('inf'):
    print(-1)
else:
    print(ans)
