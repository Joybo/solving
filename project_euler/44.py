# http://projecteuler.net/problem=44
#
# j = 1019
# k = 2166
# Pj = 1560090
# Pk = 7042750
# Answer: 7042750 - 1560090 = 5482660
# This code is a bruce-force by guess.

def pentagonal():
  res_list = [1]
  res_dict = {1:1}

  index = 2
  prev = 1
  d = 4
  while d <= 8000:
    next = prev + d
    res_list += [next]
    res_dict[next] = index

    prev = next
    d += 3
    index += 1
  return res_list, res_dict

p_list, p_dict = pentagonal()
p_size = len(p_list)

min_pos = 2000
for j in xrange(0, p_size):
  for k in xrange(j+1, p_size):
    if k - j > min_pos: break

    #if p_dict.has_key(p_list[j]+p_list[k]):
    #  min_pos = k - j + 1

    if p_dict.has_key(p_list[j]+p_list[k]) and p_dict.has_key(p_list[k]-p_list[j]):
      print j, k, p_list[j], p_list[k]
