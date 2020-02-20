def calculate(n):
    ans = 0
    for i in range(len(str(n))):
        ans += n % 10
        n //= 10
    return ans


n = int(input())
if n % calculate(n) == 0:
    print('Yes')
else:
    print('No')