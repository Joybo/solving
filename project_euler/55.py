# http://projecteuler.net/problem=55
# Answer: 249
# Time: 0.202332019806

from common import cal_time, reverse_num, is_palindrome

def is_lychrel(n):
  for i in xrange(24):
    n += reverse_num(n)
    if is_palindrome(n): return False

  return True

@cal_time
def get_ans():
  ans = 0
  for i in xrange(10000):
    if is_lychrel(i):
      ans += 1

  return ans

get_ans()

