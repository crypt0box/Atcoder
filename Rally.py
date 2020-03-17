n = int(input())
x = list(map(int, input().split()))
ans = float('inf')
energy = []

for i in range(1, 101):
    for j in x:
        energy.append((j - i) ** 2)
    sum_energy = sum(energy)
    if sum_energy < ans:
        ans = sum_energy
    energy = []

print(ans)
