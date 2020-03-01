n = int(input())
blu_list = [str(input()) for _ in range(n)]
m = int(input())
red_list = [str(input()) for _ in range(m)]

blu_set_list = list(set(blu_list))
red_set_list = list(set(red_list))
set_list = blu_set_list + red_set_list

blu_cnt = []
red_cnt = []
ans = []

for i in set_list:
    blu_cnt.append(blu_list.count(i))
    red_cnt.append(red_list.count(i))

for i in range(len(set_list)):
    ans.append(blu_cnt[i] - red_cnt[i])

print(max(ans) if max(ans) > 0 else 0)
