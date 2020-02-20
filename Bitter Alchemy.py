n, x = map(int, input().split())
m = [int(input()) for i in range(n)]
rem_donut = x - sum(m)
add_donut = rem_donut // min(m)
print(add_donut + n)