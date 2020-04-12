n = int(input())
ans = []
num = 0

for i in range(1, n+1):
    if i % 3 == 0 and i % 5 == 0:
        ans.append('FizzBuzz')
    elif i % 3 == 0:
        ans.append('Fizz')
    elif i % 5 == 0:
        ans.append('Buzz')
    else:
        num += i
print(num)