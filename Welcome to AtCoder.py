n, m = map(int, input().split())

p = [str(input()) for _ in range(m)]

for i in range(m):
    if str(i + 1) in p[i]:
