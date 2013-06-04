# http://projecteuler.net/problem=56
# Answer: 972
# Time: 0.376945972443
# Performance: n ** m > mypow(n, m) > mypow2(n, m)

from common import cal_time

def sum_digit(n):
  ans = 0
  while n > 0:
    ans += (n%10)
    n /= 10
  return ans

def mypow(n, m):
  if m == 0: return 1
  if m == 1: return n
  t = mypow(n, m >> 1)
  return t * t * n if m % 2 else t * t

def mypow2(n, m, d = {}):
  if m == 0: return 1
  if m == 1: return n
  m >>= 1
  t = d.get(m, mypow(n, m))
  return t * t * n if m % 2 else t * t

@cal_time
def get_ans():
  max_sum = 0
  for a in xrange(100):
    for b in xrange(100):
      sum_val = sum(map(int, list(str(a ** b))))
      #sum_val = sum(map(int, list(str(mypow(a, b)))))
      #sum_val = sum_digit(a ** b)
      #sum_val = sum_digit(mypow(a, b))
      if sum_val > max_sum:
        max_sum = sum_val

  return max_sum

get_ans()
