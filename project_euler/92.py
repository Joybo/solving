# http://projecteuler.net/problem=92
# Answer: 8581146
# Time: 65.5761039257

from common import cal_time

def get_digit_square(n):
  res = 0
  for ch in str(n):
    v = int(ch)
    res += (v ** 2)
  return res

@cal_time
def get_ans():
  cache = {
    1:0, 10:0, 13:0, 32:0, 44:0, 
    4:1, 16:1, 20:1, 37:1, 42:1, 58:1, 85:1, 89:1, 145:1,
  }

  for i in xrange(2, 10000001):
    if cache.has_key(i): continue

    chain = [i]
    next = i
    while True:
      next = get_digit_square(next)

      if cache.has_key(next):
        is89 = cache[next]
        for j in chain: cache[j] = is89
        break

      if next in chain:
        for j in chain: cache[j] = 0
        break

      chain += [next]

  return sum([cache[k] for k in cache.keys()])

get_ans()
