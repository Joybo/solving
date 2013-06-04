# http://projecteuler.net/problem=63
# Answer: 49
# Time: 0.0531690120697

from common import cal_time, get_digit

@cal_time
def get_ans():
  ans = 0
  for i in xrange(1, 100):
    for j in xrange(1, 100):
      if get_digit(i ** j) == j: ans +=1

  return ans

get_ans()
