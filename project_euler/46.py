# http://projecteuler.net/problem=46
# Answer: 5777

from common import is_prime

def is_pass(n):
  i = 0
  while True:
    twice_square = 2 * i * i
    if twice_square >= n: break
    if is_prime(n - twice_square):
      return True
    i += 1

  return False

n = 1
while True:
  n += 2
  if not is_pass(n):
    print n, "fail"
    break


