n = int(input())
s = list(str(input()))
ans = []
for i in range(len(s)):
    ans.append(chr(ord(s[i]) + n))
    if ord(s[i]) + n > 90:
        ans[i] = chr(ord(s[i]) + n - 26)
print("".join(ans))
