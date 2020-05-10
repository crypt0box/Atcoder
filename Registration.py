s = str(input())
t = str(input())

print('Yes' if len(s) == len(t) -1 and s == t[:-1] else 'No')