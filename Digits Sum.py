def calculate(n):
    ans = 0
    for i in range(len(str(n))):
        ans += n % 10
        n //= 10
    return ans


n = int(input())
val = 100000
num = []
for i in range(1, n):
    num.append([i, n-i])
    cal = calculate(num[i-1][0]) + calculate(num[i-1][1])
    if val > cal:
        val = cal
print(val)
