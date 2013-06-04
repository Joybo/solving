from decorator import decorator
@decorator
def cal_time(func, *args, **kwargs):
  import time
  now = time.time()
  print('Answer: {0}'.format(func(*args, **kwargs)))
  print('Time: {0}'.format(time.time() -  now))

def sieve_list(n):
  t = [1] * (n + 1)
  t[0] = t[1] = 0
  for i in xrange(4, n + 1, 2): t[i] = 0
  for i in xrange(3, n + 1, 2):
    if t[i] == 0: continue
    for j in xrange(i + i, n + 1, i): t[j] = 0

  return t

def sieve_prime(n):
  t = sieve_list(n)
  return [i for i in xrange(n + 1) if t[i]]

def is_prime(n):
  if n < 2: return False
  if n <= 3: return True
  if n % 2 == 0: return False

  ori_n = n

  i = 3
  while i * i <= ori_n:
    if n % i == 0:
      return False
    i += 2

  return True

def get_factor(n):
  res = []
  if n % 2 == 0:
    res += [2]
    while n % 2 == 0: n /= 2

  i = 3
  while i * i <= n:
    if n % i == 0:
      res += [i]
      while n % i == 0: n /= i
    i += 2

  if n > 1: res += [n]
  return res

def get_factor_value(n):
  res = 1
  for i in xrange(n, 1, -1):
    res *= i
  return res

def mypow(n, m):
  if m == 0: return 1
  if m == 1: return n
  t = mypow(n, m >> 1)
  return t * t * n if m % 2 else t * t

# Performance: mypow > mypow2
def mypow2(n, m, d = {}):
  if m == 0: return 1
  if m == 1: return n
  m >>= 1
  t = d.get(m, mypow(n, m))
  return t * t * n if m % 2 else t * t

def pow_mod(n, m, mod):
  if m == 0: return 1
  if m == 1: return n % mod
  t = mypow(n, m >> 1)
  return (t * t * n)%mod if m % 2 else (t * t)%mod

def get_digit(n):
  return len(str(n))

def is_perm(n1, n2):
  n1_list = list(str(n1))
  n2_list = list(str(n2))
  n1_list.sort()
  n2_list.sort()
  return n1_list == n2_list

def reverse_num(val):
  val = list(str(val))
  val.reverse()
  return int(''.join(val))

def is_palindrome(val):
  return val == reverse_num(val)

def read_file(file_name):
  with open(file_name, 'rb') as fr:
    return fr.read()

def concat_nums(*args):
  return int(''.join(map(str, args)))

