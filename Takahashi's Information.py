# 参考：sssssssiiiiinnnさん
import numpy as np
import sys


def validation(c, a, b):
    for i in range(3):
        for j in range(3):
            if c[i][j] != a[i] + b[j]:
                print('No')
                return sys.exit()
    print('Yes')
    return sys.exit()


c_1 = list(map(int, input().split()))
c_2 = list(map(int, input().split()))
c_3 = list(map(int, input().split()))
c = np.array([c_1, c_2, c_3])
for i in range(np.max(c)+1):
    a = []
    b = []
    a.append(i)
    b.append(c[0][0] - a[0])
    b.append(c[0][1] - a[0])
    b.append(c[0][2] - a[0])
    a.append(c[1][0] - b[0])
    a.append(c[2][0] - b[0])
    validation(c, a, b)

