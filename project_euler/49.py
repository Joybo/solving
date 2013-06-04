# http://projecteuler.net/problem=49
# Answer: 296962999629

from common import cal_time, is_prime

def is_perm(n1, n2):
  return sorted(list(str(n1))) == sorted(list(str(n2)))

@cal_time
def get_ans():
  maximum = 10000 - 3330 * 2
  for i in xrange(1487 + 2, maximum, 2):
    if not is_prime(i): continue

    j = i + 3330
    if not is_prime(j) or not is_perm(i, j): continue
    k = j + 3330
    if not is_prime(k) or not is_perm(i, k): continue
    return '{0}{1}{2}'.format(i, j, k)

get_ans()
