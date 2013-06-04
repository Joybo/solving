# http://projecteuler.net/problem=58
# Answer: 26241
# Time: 11.5268411636

from common import cal_time, is_prime

@cal_time
def get_ans():
  item = [1]
  item_size = 1
  prime_count = 0
  
  offset = 0
  diff = 0
  while True:
    diff += 2
    for _ in xrange(4):
      next_item = item[offset] + diff
      if is_prime(next_item):
        prime_count += 1

      item += [next_item]
      offset += 1

    item_size += 4

    if float(prime_count) / item_size < 0.1:
      return diff + 1

get_ans()
