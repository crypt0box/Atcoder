a, b = map(int, input().split())
ans = []
for i in range(b-a+1):
    num = list(map(str, str(a + i)))
    if num[0] == num[4] and num[1] == num[3]:
        ans.append(int("".join(num)))
print(len(ans))