# 1A - Theater Square
# http://codeforces.com/problemset/problem/1/A
# AC
from math import ceil
n, m, a = map(float, raw_input().split())
ans = ceil(n/a) * ceil(m/a)
print(int(ans))

