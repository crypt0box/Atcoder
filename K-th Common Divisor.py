a, b, k = map(int, input().split())


def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    divisors.sort()
    return divisors


a_div = make_divisors(a)
b_div = make_divisors(b)
div_list = a_div + b_div

ans = sorted([x for x in set(div_list) if div_list.count(x) > 1])

print(ans[-k])
