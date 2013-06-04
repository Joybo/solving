# http://projecteuler.net/problem=53
# Answer: 4075
# Time: 0.0500011444092

from common import cal_time, get_factor_value

@cal_time
def get_ans():
  ans = 0

  for n in xrange(1, 101):
    for r in xrange(1, n+1):
      if r > n-r: break

      val = get_factor_value(n) / get_factor_value(r) / get_factor_value(n-r)
      if val > 1000000: 
        ans += 1
        if n-r != r: ans += 1

  return ans

get_ans()
