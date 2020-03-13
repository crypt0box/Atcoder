n = int(input())
digit_list = []
cnt = 0

for i in range(1, n+1):
    digit_list.append(len(str(i)))

for i in digit_list:
    if i % 2 == 1:
        cnt += 1

print(cnt)