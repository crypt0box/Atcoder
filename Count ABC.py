n = int(input())
s = str(input())
cnt = 0

for i in range(n):
    if s[i : i + 3] == 'ABC':
        cnt += 1

print(cnt)
