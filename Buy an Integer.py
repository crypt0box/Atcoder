a, b, x = map(int, input().split())
for i in range(1,1000000001):
    val = x - (a * i + b * len(str(i)))
    if val <= 0:
        ans = i-1
        break
print(ans)
# とけませんでした・・・・。
# 方程式が単調増加のため２分探索できるらしい
