# http://projecteuler.net/problem=97
# Answer: 8739992577
# Time: 0.104197978973
# Notice: Need use pow_mod

from common import cal_time, pow_mod

@cal_time
def get_ans():
  return str(28433 * pow_mod(2, 7830457, 10 ** 10) + 1)[-10:]

get_ans()
