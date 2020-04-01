n, m = map(int, input().split())

n_cmb = n * (n - 1) / 2
m_cmb = m * (m - 1) / 2
print(int(n_cmb + m_cmb))
