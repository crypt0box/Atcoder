x = int(input())

yen_500 = x // 500
yen = x % 500
yen_5 = yen // 5

print(yen_500 * 1000 + yen_5 *5)