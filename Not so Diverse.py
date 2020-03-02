import collections

n, k = map(int, input().split())
a = list(map(int, input().split()))
ans = 0

list_a = list(collections.Counter(a).values())
dic = dict(zip(collections.Counter(a), list_a))
dic_sorted = sorted(dic.items(), key=lambda x: x[1])
del_num = dic_sorted[:len(dic_sorted)-k]

for i in del_num:
    ans += i[1]

print(ans)
