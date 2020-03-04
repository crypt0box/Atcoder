a, b, c, x, y = map(int, input().split())

if a + b < 2 * c:
    ans = a * x + b * y
    print(ans)
else:
    if x < y:
        ans = (y - x) * b + c * 2 * x
        print(ans if ans < 2 * c * y else 2 * c * y)
    else:
        ans = (x - y) * a + c * 2 * y
        print(ans if ans < 2 * c * x else 2 * c * x)
