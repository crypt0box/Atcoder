n = int(input())

d = {}
for i in range(n):
    s = input()
    if s in d:
        d[s] += 1
    else:
        d[s] = 1

m = max(d.values())
for i in sorted(k for k in d if d[k] == m):
    print(i)

