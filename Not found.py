S = str(input())
ans = 'None'
alfabet = 'abcdefghijklmnopqrstuvwxyz'
for i in alfabet:
    if i not in S:
        ans = i
        break
print(ans)
