# http://projecteuler.net/problem=3
# Answer: 6857

def get_factor(n):
  res = []
  if n % 2 == 0:
    res += [2]
    while n % 2 == 0: n /= 2

  i = 3
  while i * i <= n:
    if n % i == 0:
      res += [i]
      while n % i == 0: n /= i
    i += 2

  if n > 1: res += [n]
  return res

print max(get_factor(n = 600851475143))
