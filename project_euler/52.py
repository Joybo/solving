# http://projecteuler.net/problem=52
# Answer: 142857
# Time: 0.537279129028

from common import cal_time, get_digit, is_perm

@cal_time
def get_ans():
  i = 0
  while True:
    i += 1
    digit = get_digit(i)
    val = i

    is_find = True
    for j in xrange(2, 7):
      val += i
      if get_digit(val)!=digit or not is_perm(i, val):
        is_find = False
        break

    if is_find:
      return i

get_ans()
