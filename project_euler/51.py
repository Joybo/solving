# http://projecteuler.net/problem=51
# Answer: 121313
# Notice:
#   1. Suffix digit must equal to 3.
#   2. Mask values * are all the same.

from common import cal_time, is_prime

def rec_primes(digit, num_digit, num_index, mark_digit, num_list, ans_list):
  if len(ans_list) == digit - 1:
    primes = []
    start_mark_value = 0 if ans_list[0]!='*' else 1
    for i in xrange(start_mark_value, 10, 1):
      val = int(''.join(ans_list + ['3']).replace('*', str(i)))
      if is_prime(val): primes += [val]
    yield primes
    return

  if num_digit + (mark_digit + 1) <=  digit:
    for primes in rec_primes(digit, num_digit, num_index, mark_digit + 1, num_list, ans_list[:] + ['*']):
      yield primes
  if num_index < num_digit:
    for primes in rec_primes(digit, num_digit, num_index+1, mark_digit, num_list, ans_list[:] + [num_list[num_index]]):
      yield primes

@cal_time
def get_ans():
  #start_digit = 5 # time: 14.2700021267
  start_digit = 6 # time: 0.0474219322205
  for digit in xrange(start_digit, 10):
    maximum = 10 ** digit
    for i in xrange(1, maximum):
      num_list = list(str(i))
      num_digit = len(str(i))
      mark_digit = digit - num_digit
      for primes in rec_primes(digit, num_digit, 0, 0, num_list, []):
        if len(primes) != 8: continue
        primes.sort()
        return primes[0]

get_ans()

