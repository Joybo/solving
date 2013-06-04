# http://projecteuler.net/problem=79
# Answer: 73162890
# Time: 0.000233888626099

from common import cal_time, read_file

def init_analyzing_list():
  res = []
  for i in xrange(10): res += [[]]
  return res

def unique_sort_analyzing_list(analyzing):
  for i in xrange(10):
    analyzing[i] = list(set(analyzing[i]))
    analyzing[i].sort()
  return analyzing

def show_analyzing_list(analyzing):
  for i in xrange(10):
    print('{0}: {1}'.format(i, analyzing[i]))

def analyze_keylogers(keylogers):
  before = init_analyzing_list()
  after = init_analyzing_list()

  for num in keylogers:
    d1 = num / 100
    d2 = (num %100) / 10
    d3 = num % 10

    # brfore
    before[d2] += [d1]
    before[d3] += [d1]
    before[d3] += [d2]

    # after
    after[d1] += [d2]
    after[d1] += [d3]
    after[d2] += [d3]

  unique_sort_analyzing_list(before)
  unique_sort_analyzing_list(after)
  #show_analyzing_list(before)
  #show_analyzing_list(after)

  weight = {}
  max_weight = 0
  for i in xrange(10): weight[i] = 0
  for i in xrange(10):
    for j in before[i]: 
      weight[j] += 1
      if weight[j] > max_weight:
        max_weight = weight[j]

  ans = []
  for i in xrange(max_weight, 0, -1):
    for j in xrange(10):
      if weight[j] == i:
        ans += [str(j)]

  for i in xrange(10):
    if weight[i]==0 and before[i]: ans += [str(i)]

  return ''.join(ans)

@cal_time
def get_ans():
  keylogers = map(int, read_file('79_keylog.txt').splitlines())
  return analyze_keylogers(keylogers)

get_ans()
