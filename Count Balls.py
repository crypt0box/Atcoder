n, a, b = map(int, input().split())

ans = n // (a + b) * a
rem = n % (a + b)
ans += min(a, rem)  # ansとremを比較することでnの位置よって処理を変えられる

print(ans)
