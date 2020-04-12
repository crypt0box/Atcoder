import math
from functools import reduce

def gcd(*numbers):
    return reduce(math.gcd, numbers)

k = int(input())
ans = 0
a = list(range(1,k+1))
b = list(range(1,k+1))
c = list(range(1,k+1))

for i in a:
    for j in b:
        for k in c:
            ans += gcd(i,j,k)
print(ans)