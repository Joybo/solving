# http://projecteuler.net/problem=57
# Answer: 153
# Time: 0.00118398666382
# You can find a formula, next num = prev num + 2 * den, next den = next num - prev den

from common import cal_time
from math import log10

@cal_time
def get_ans():
  ans = 0

  num, den = 1, 1
  for i in xrange(1000):
    num += (2 * den)
    den = num - den

    if int(log10(num)) > int(log10(den)):
      ans += 1
      
  return ans

get_ans()
