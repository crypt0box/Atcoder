s = str(input())
cnt = 0
cnt_list = []

for i in range(len(s)):
    if s[i] in 'ACGT':
        cnt += 1
        cnt_list.append(cnt)
    else:
        cnt = 0
        cnt_list.append(0)
print(max(cnt_list))