# http://projecteuler.net/problem=47
#

from common import cal_time,get_factor

@cal_time
def get_ans():
  i = 1
  while True:
    if len(get_factor(i))==4 and len(get_factor(i+1))==4 and len(get_factor(i+2))==4 and len(get_factor(i+3))==4:
      return i
      break
    i += 1

get_ans()
