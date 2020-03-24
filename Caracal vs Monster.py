h = int(input())

ans = 0
cnt = 1
for i in range(100):
    if h == 1:
        break
    else:
        h = int(h / 2)
        cnt *= 2
    ans += cnt
print(ans + 1)