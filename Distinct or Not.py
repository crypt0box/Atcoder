import collections

n = int(input())
a = list(map(int, input().split()))

a_dict = collections.Counter(a)

if max(a_dict.values()) > 1:
    print('NO')
else:
    print('YES')
