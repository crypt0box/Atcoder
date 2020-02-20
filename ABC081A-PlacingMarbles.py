from sys import stdin

ans = 0
s = list(stdin.readline().rstrip())

for i in s:
    if i == "1":
        ans += 1

print(ans)