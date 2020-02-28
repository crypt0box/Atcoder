N, M = map(int, input().split())
num_listP = [list(map(int, input().split())) for _ in range(M)]
num_list = [e for row in num_listP for e in row]

ans = []
cnt = 0

for i in range(1, N+1):
    ans.append(cnt)
    cnt = 0
    for j in num_list:
        if i == j:
            cnt += 1

ans.append(cnt)
for i in range(1, N+1):
    print(ans[i])
