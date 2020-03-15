# 屈辱的ウンコードいつか綺麗に書けるように
a1 = list(map(int, input().split()))
a2 = list(map(int, input().split()))
a3 = list(map(int, input().split()))
a = a1 + a2 + a3
n = int(input())
b = [int(input()) for i in range(n)]

for i in b:
    if i in a:
        a[a.index(i)] = 0

if a[0] == a[1] == a[2] == 0:
    print('Yes')
elif a[3] == a[4] == a[5] == 0:
    print('Yes')
elif a[6] == a[7] == a[8] == 0:
    print('Yes')
elif a[0] == a[3] == a[6] == 0:
    print('Yes')
elif a[1] == a[4] == a[7] == 0:
    print('Yes')
elif a[2] == a[5] == a[8] == 0:
    print('Yes')
elif a[0] == a[4] == a[8] == 0:
    print('Yes')
elif a[2] == a[4] == a[6] == 0:
    print('Yes')
else:
    print('No')
