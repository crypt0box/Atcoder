x = int(input())
fukuri = 0
ans = 100

for i in range(5000):
    fukuri = int(ans * 0.01)
    ans += fukuri
    if ans >= x:
        print(i+1)
        break
