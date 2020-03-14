h, w = map(int, input().split())

if h * w % 2 == 0:
    ans = h * w / 2
else:
    ans = h * w // 2 + 1

if h == 1 or w == 1:
    ans = 1

print(int(ans))
