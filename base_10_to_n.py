def base_10_to_n(x, n):
    if int(x/n):
        return base_10_to_n(int(x/n), n)+str(x % n)
    return str(x % n)
