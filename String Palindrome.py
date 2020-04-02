s = str(input())
n = len(s)

if s[:int((n-1)/2)] == s[int((n-1)/2+1):]:
    print('Yes')
else:
    print('No')
