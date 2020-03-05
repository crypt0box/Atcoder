n = int(input())
ans = []


# 約数の計算
def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)
    divisors.sort()
    return divisors


for a in make_divisors(n):
    b = int(n / a)
    if len(str(a)) <= len(str(b)):
        ans.append(len(str(b)))

print(min(ans))
