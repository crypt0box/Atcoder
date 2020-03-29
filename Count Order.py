import itertools

n = int(input())
p = tuple(map(int, input().split()))
q = tuple(map(int, input().split()))


n_list = list(range(1, n+1))
n_perm = list(itertools.permutations(n_list))

print(abs(n_perm.index(p) - n_perm.index(q)))
