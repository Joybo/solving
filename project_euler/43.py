# http://projecteuler.net/problem=43
# Answer: 16695334890

from common import cal_time

res = []

def check_ans(d = []):
  if (d[2]*100 + d[3]*10 + d[4]) % 2 == 0 and \
     (d[3]*100 + d[4]*10 + d[5]) % 3 == 0 and \
     (d[4]*100 + d[5]*10 + d[6]) % 5 == 0 and \
     (d[5]*100 + d[6]*10 + d[7]) % 7 == 0 and \
     (d[6]*100 + d[7]*10 + d[8]) % 11 == 0 and \
     (d[7]*100 + d[8]*10 + d[9]) % 13 == 0 and \
     (d[8]*100 + d[9]*10 + d[10]) % 17 == 0:
       global res
       res += [
         int(''.join(map(str, d)))
       ]

def rec_pandigital(index, d = [], used = []):
  if index > 10:
    check_ans(d)
    return

  for i in xrange(0, 10):
    if not used[i]:
      if index==4 and i%2!=0: continue
      elif index==5 and (d[3]+d[4]+i)%3!=0: continue
      elif index==6 and i%5!=0: continue
      elif index==7 and (d[5]*100 + d[6]*10 + i) % 7: continue
      elif index==8 and (d[6]-d[7]+i)%11: continue

      d[index] = i
      used[i] = 1
      rec_pandigital(index + 1, d, used)
      used[i] = 0

@cal_time
def method1():
  rec_pandigital(1, [0] * 11, [0] * 11)
  #res = [1406357289, 1430952867, 1460357289, 4106357289, 4130952867, 4160357289]
  return sum(res)

def method2():
  from itertools import permutations
  for d in permutations([1,2,3,4,5,6,7,8,9,0]):
    d = [0] + list(d)
    check_ans(d)

  print res
  print sum(res)

method1()
#method2()
