import numpy as np

w, h, n = map(int, input().split())
num_list = np.array([[1 for _ in range(w)] for _ in range(h)])

for i in range(n):
    x, y, a = map(int, input().split())
    if a == 1:
        num_list[:, :x] = 0
    elif a == 2:
        num_list[:, x-1:] = 0
    elif a == 3:
        num_list[:y-1, :] = 0
    else:
        num_list[y:, :] = 0

print(sum(sum(num_list)))

