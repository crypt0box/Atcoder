a, b, c = map(int, input().split())

if 4 * a * b < (c - a - b) ** 2 and 0 <= c - a - b:
    ans = 'Yes'
else:
    ans = 'No'

print(ans)

