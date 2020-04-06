num = list(map(int, input().split()))
num_set = set(num)

print('Yes' if len(num_set) == 2 else 'No')
